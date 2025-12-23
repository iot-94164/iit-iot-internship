#include <WiFi.h>
#include <ArduinoMqttClient.h>

const char *ssid = "OPPO A16k";
const char *password = "123456789";

const char *broker = "172.18.4.146";
const int port = 1883;

WiFiClient wifiClient;
MqttClient mqttClient(wifiClient);

void setup() {
  Serial.begin(115200);

  pinMode(2, OUTPUT);
  digitalWrite(2, LOW);

  // Connect WiFi
  WiFi.begin(ssid, password);
  Serial.print("Connecting to WiFi");

  while (WiFi.status() != WL_CONNECTED) {
    delay(500);
    Serial.print(".");
  }

  Serial.println("\nWiFi connected");
  Serial.print("ESP32 IP: ");
  Serial.println(WiFi.localIP());

  // Connect MQTT Broker
  Serial.print("Connecting to MQTT broker...");
  if (!mqttClient.connect(broker, port)) {
    Serial.println(" failed!");
    while (1);
  }
  Serial.println(" connected");

  // Subscribe topic
  mqttClient.subscribe("room/light");
  Serial.println("Subscribed to topic: room/light");
}

void loop() {
  mqttClient.poll();   // IMPORTANT for MQTT

  int messageSize = mqttClient.parseMessage();
  if (messageSize) {
    String msg = "";

    while (mqttClient.available()) {
      msg += (char)mqttClient.read();
    }

    Serial.print("Received: ");
    Serial.println(msg);

    if (msg == "ON") {
      digitalWrite(2, HIGH);
      Serial.println("LED ON");
    }
    else if (msg == "OFF") {
      digitalWrite(2, LOW);
      Serial.println("LED OFF");
    }
  }
}
