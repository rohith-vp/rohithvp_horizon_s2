#include <Servo.h>

Servo servo;

// Servo motor position
int pos;

// Potentiometer
int potPin = A0;
int potVal = 0;
int lastPotVal = 0;
int potAngle = 0;

// Potentiometer Angle Warning LED
int ledPin = 10;

void setup()
{
  Serial.begin(9600);
  servo.attach(9);    // Initialize sevro motor
  servo.write(0);     // Set servo motor to 0degrees
  pinMode(ledPin, OUTPUT);
}

void loop()
{
  // Read current potentiometer value
  potVal = analogRead(potPin);
  
  // Check if potentiometer value changed
  if (potVal != lastPotVal) {
    potAngle = map(potVal, 0, 1023, 0, 180);    // Convert pot value to angle (0 - 180 degrees)
  	Serial.print("Potentiometer angle: ");
    Serial.println(potAngle);
    lastPotVal = potVal;
    
    // Don't let the servo motor go above 68 degrees
    if (potAngle > 68) {
      Serial.println("Servo limit reached.");
      digitalWrite(ledPin, HIGH);   // Turn on warning LED
    // Set motor angle is angle is less than 68 degrees
    } else {
    	servo.write(potAngle);
      digitalWrite(ledPin, LOW);   // Turn off warning LED
    }
  }

  delay(10);
}