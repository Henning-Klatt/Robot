#include <Servo.h>
Servo servo_x;
Servo servo_y;

int intLoopCounter = 0;
String strSerialInput = "";

void setup() {
  servo_x.attach(2); //Servo 1 an PIN 2 | min: 12 | max: 180 | norm: 101
  servo_y.attach(3); //Servo 2 an PIN 3 | min: 10 | max: 180 | norm: 100
  Serial.begin(57600);  //Serieller Port on 57600
  Serial.println("Initalisiert!");
}

String getValue(String data, char separator, int index)
{
  int found = 0;
  int strIndex[] = {0, -1};
  int maxIndex = data.length()-1;

  for(int i=0; i<=maxIndex && found<=index; i++){
    if(data.charAt(i)==separator || i==maxIndex){
        found++;
        strIndex[0] = strIndex[1]+1;
        strIndex[1] = (i == maxIndex) ? i+1 : i;
    }
  }

  return found>index ? data.substring(strIndex[0], strIndex[1]) : "";
}

void loop() {
  //Nicht zu viel Stress
  delay(1);
  ExecuteSerialCommand();
}

void ExecuteSerialCommand(){
  String serialData = GetPossibleSerialData();

  if(serialData != "") {

    /* RAW Data Construction:

    01      1     180
    ---------------------
    Aktor   AN    Stärke
    Servo 1 AN    Grad
    Motor 1 Links 100% Geschwindigkeit
    Licht 1 AN    100% Helligkeit
    
    */
    
    Serial.print("\nRaw Data: " + serialData);

    int Aktor = getValue(serialData, ',', 0).toInt();
    int Status = getValue(serialData, ',', 1).toInt();
    int Aktion = getValue(serialData, ',', 2).toInt();

    switch (Aktor) {
      
      case 1: //Servo X
        if((Aktion >= 0) && (Aktion <= 180)) {
          Aktion = map(Aktion, 0, 180, 12, 180);
          servo_x.write(Aktion);
        }
        break;
        
       case 2: //Servo Y
        if((Aktion >= 0) && (Aktion <= 180)) {
          Aktion = map(Aktion, 0, 180, 10, 180);
          servo_y.write(Aktion);
        }
        break;

       case 3: //Motor A /Links
        if((Aktion >= 0) && (Aktion <= 100)) {
          Serial.print("\nMotor 1: " + Aktion);
        }
        break;
        
      default:
        Serial.print("\nGebe Bitte einen Aktor an!");
    }
  }
}

String GetPossibleSerialData() {
  String retVal;
  int iteration = 10; 
  if(strSerialInput.length() > 0) {
    if(intLoopCounter > strSerialInput.length() + iteration) {
      retVal = strSerialInput;
      strSerialInput = "";
      intLoopCounter = 0;
    }
    intLoopCounter++;
  }

  return retVal;
}

void serialEvent() {
  while(Serial.available()) {
    strSerialInput.concat((char) Serial.read());
  }
}
