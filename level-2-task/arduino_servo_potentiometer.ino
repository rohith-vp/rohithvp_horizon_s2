#include <Servo.h>

Servo servo;

int pos;

int potPin = A0;
int potVal = 0;
int lastPotVal = 0;
int potAngle = 0;

int ledPin = 10;

void setup()
{
  Serial.begin(9600);
  servo.attach(9);
  servo.write(0);
  pinMode(ledPin, OUTPUT);
}

void loop()
{
  potVal = analogRead(potPin);
  
  if (potVal != lastPotVal) {
    potAngle = map(potVal, 0, 1023, 0, 180);
  	Serial.print("Potentiometer angle: ");
    Serial.println(potAngle);
    lastPotVal = potVal;
    
    if (potAngle > 68) {
    	Serial.println("Servo limit reached.");
      	digitalWrite(ledPin, HIGH);
    } else {
    	servo.write(potAngle);
      	digitalWrite(ledPin, LOW);
    }
  }
  
  delay(10);
}