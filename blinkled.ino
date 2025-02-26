void setup() {
  Serial.begin(9600);
  pinMode(13, OUTPUT);  // Set GPIO 2 as an output
  pinMode(12, OUTPUT);
}

void loop() {
  digitalWrite(12, HIGH);  // Turn LED ON
  Serial.println("LED is ON");  // Print to Serial Monitor
  delay(500);  // Wait 1 second

  digitalWrite(12, LOW);   // Turn LED OFF
  Serial.println("LED is OFF");  // Print to Serial Monitor
  delay(500);  // Wait 1 second

  digitalWrite(13, HIGH);  // Turn LED ON
  Serial.println("LED is ON");  // Print to Serial Monitor
  delay(500);  // Wait 1 second

  digitalWrite(13, LOW);   // Turn LED OFF
  Serial.println("LED is OFF");  // Print to Serial Monitor
  delay(500);  // Wait 1 second


}
