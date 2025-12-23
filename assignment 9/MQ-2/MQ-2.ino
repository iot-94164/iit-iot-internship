#define MQ2_PIN 34   // Analog pin connected to MQ-2

void setup() {
  Serial.begin(9600);
  pinMode(MQ2_PIN, INPUT);
}

void loop() {
  int gasValue = analogRead(MQ2_PIN);

  Serial.print("MQ-2 Gas Sensor Value: ");
  Serial.println(gasValue);

  // Simple condition
  if (gasValue > 2000) {
    Serial.println("⚠️ Gas Detected!");
  } else {
    Serial.println("✅ Gas Level Normal");
  }

  delay(1000);
}