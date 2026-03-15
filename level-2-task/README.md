# LEVEL 2 Task: Arduino Simulation

### Project Overview

This task involves connecting a servo motor and poteniometer to an arduino uno, and controlling the servo motor with the potentiometer, while restricting the servo motor to 68 degrees.

### Files

* **arduino_servo_potentiometer.ino:** Arduino code for TinkerCad simulation  
* **tinkercad.mp4:** Video showing TinkerCad simulation

### TinkerCad Circuit Link

https://www.tinkercad.com/things/agoVIbNgxMs-horizon-task-level-2?sharecode=YXgpA6qSjDxgFkdXY2Uuu3Miv5cIi9g9arVP8PQ-1dc

### Circuit Components

* Arduino Uno R3
* Servo Motor
* Potentiometer
* LED
* 100 Ohm Resistor

### Functional Requirements and Logic

* Map analog input (0-1023) from potentiometer (A0) to angle (0-180)
* If angle <= 68 degrees, move the servo motor (D9) to that angle
* If angle > 68, dont move the servo motor and turn on warning LED (D10)