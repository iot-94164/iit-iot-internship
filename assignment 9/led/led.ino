#define LED_BUILTIN 2
void setup() {
  pinMode(LED_BUILTIN, OUTPUT);   // Set LED pin as output
}

void loop() {
  digitalWrite(LED_BUILTIN, HIGH); // LED ON
  delay(1000);                     // wait 1 second
  digitalWrite(LED_BUILTIN, LOW);  // LED OFF
  delay(1000);                     // wait 1 second
}

