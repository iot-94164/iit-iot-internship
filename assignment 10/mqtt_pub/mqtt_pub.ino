#include <WiFi.h>
#include <ArduinoMqttClient.h>
#include <DHT.h>

/* WiFi credentials */
const char *ssid = "SUNBEAM";
const char *password = "1234567890";

/* MQTT Broker details */
const char *broker = "172.18.4.146";
int port = 1883;

/* DHT Sensor */
#define DHT_PIN 4
#define DHT_TYPE DHT11

DHT dht(DHT_PIN, DHT_TYPE);

/* WiFi & MQTT client */
WiFiClient wifiClient;
MqttClient mqttClient(wifiClient);

void setup() {
  Serial.begin(115200);
  dht.begin();

  /* Connect to WiFi */
  WiFi.mode(WIFI_STA);
  WiFi.begin(ssid, password);

  Serial.print("Connecting to WiFi");
  while (WiFi.status() != WL_CONNECTED) {
    delay(500);
    Serial.print(".");
  }

  Serial.println("\nWiFi Connected");
  Serial.print("IP Address: ");
  Serial.println(WiFi.localIP());

  /* Connect to MQTT broker */
  Serial.print("Connecting to MQTT broker...");
  while (!mqttClient.connect(broker, port)) {
    Serial.print(".");
    delay(1000);
  }
  Serial.println("\nMQTT Connected");
}

void loop() {
  float temperature = dht.readTemperature();   // Celsius
  float humidity = dht.readHumidity();

  if (isnan(temperature) || isnan(humidity)) {
    Serial.println("Failed to read from DHT sensor!");
    delay(2000);
    return;
  }

  /* Publish temperature */
  mqttClient.beginMessage("sensor/temperature");
  mqttClient.print(temperature);
  mqttClient.endMessage();

  /* Publish humidity */
  mqttClient.beginMessage("sensor/humidity");
  mqttClient.print(humidity);
  mqttClient.endMessage();

  Serial.print("Temperature: ");
  Serial.print(temperature);
  Serial.print(" °C  |  Humidity: ");
  Serial.print(humidity);
  Serial.println(" %");

  delay(5000);   // publish every 5 seconds
}
