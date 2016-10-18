#include <Servo.h>
Servo servoblau;
int incomingByte = 0;   // for incoming serial data

void setup() {
  servoblau.attach(2); //Servo 1 an PIN 2 | min: 12 | max: 180 | norm: 101
  //Servo 2 an PIN 3 | min: 10 | max: 180 | norm: 100
  Serial.begin(9600);  //Serieller Port on 9600
}
 

void loop() {
// send data only when you receive data:
        if (Serial.available() > 0) {
                Serial.print("I received: ");
                int servo1 = Serial.parseInt();
                Serial.println(servo1);
                servoblau.write(servo1);
                delay(3000);
        }
                
}
