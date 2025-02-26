void setup() {
  pinMode(12, OUTPUT);  // Set GPIO 12 as an output for LED
  pinMode(13, OUTPUT);  // Set GPIO 13 as an output for LED
  pinMode(16, INPUT);   // Set GPIO 16 as an input for the push button
}

void loop() {
  int logic_state = digitalRead(16); // Read button state
  
  if (logic_state == HIGH) {   // If button is pressed
    digitalWrite(12, HIGH);    // Turn ON LED on pin 12
    digitalWrite(13, HIGH);    // Turn ON LED on pin 13
  } else {
    digitalWrite(12, LOW);     // Turn OFF LED on pin 12
    digitalWrite(13, LOW);     // Turn OFF LED on pin 13
  }
}

// void setup() {
//   pinMode(12, OUTPUT);
// }

// void loop() {
//   digitalWrite(12, LOW); // LED ON
// }