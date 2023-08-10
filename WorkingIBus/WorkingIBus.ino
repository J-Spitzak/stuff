/*
  ReadAnalogVoltage

  Reads an analog input on pin 0, converts it to voltage, and prints the result to the Serial Monitor.
  Graphical representation is available using Serial Plotter (Tools > Serial Plotter menu).
  Attach the center pin of a potentiometer to pin A0, and the outside pins to +5V and ground.

  This example code is in the public domain.

  https://www.arduino.cc/en/Tutorial/BuiltInExamples/ReadAnalogVoltage
*/
/*
// the setup routine runs once when you press reset:
void setup() {
  // initialize serial communication at 9600 bits per second:
  Serial.begin(9600);
}

// the loop routine runs over and over again forever:
void loop() {
  // read the input on analog pin 0:
  int sensorValue = analogRead(A0);
  // Convert the analog reading (which goes from 0 - 1023) to a voltage (0 - 5V):
  float voltage = sensorValue * (5.0 / 1023.0);
  // print out the value you read:
  Serial.println(voltage);
}

*/
#include <IBusBM.h>
#include <Servo.h>

IBusBM ibusRc;

HardwareSerial& ibusRcSerial = Serial1;
HardwareSerial& debugSerial = Serial;


Servo LEFT;
Servo RIGHT;





void setup() {
  LEFT.attach(5);
  RIGHT.attach(6);

  ibusRc.begin(ibusRcSerial);
  debugSerial.begin(9600);
}

// Read the number of a given channel and convert to the range provided.
// If the channel is off, return the default value
int readChannel(byte channelInput, int minLimit, int maxLimit, int defaultValue){
  uint16_t ch = ibusRc.readChannel(channelInput);
  if (ch < 100) return defaultValue;
  return map(ch, 1000, 2000, minLimit, maxLimit);
}

// Red the channel and return a boolean value
bool redSwitch(byte channelInput, bool defaultValue){
  int intDefaultValue = (defaultValue)? 100: 0;
  int ch = readChannel(channelInput, 0, 100, intDefaultValue);
  return (ch > 50);
}

void loop() {

  int LV;
  int LH;
  int RV;
  int RH;

  //printing data
  for (byte i = 0; i<4; i++){
    int value = readChannel(i, -100, 100, 0);
    debugSerial.print("Ch");
    debugSerial.print(i + 1);
    debugSerial.print(": ");
    debugSerial.print(value);
    debugSerial.print(" ");

    if (i == 1){
      RV = value;
    }
    else if (i == 2){
      RH = value;
    }
    else if (i == 3){
      LV = value;
    }
    else if (i == 4){
      LH = value;
    }
  }
  debugSerial.print("Ch5: ");
  debugSerial.print(redSwitch(4, false));
  debugSerial.println();
  int DriveL;
  int DriveR;

  int forward = LV;
  int turn = RH / 2;

  if ((forward + turn) > 100){
    
  }

  delay(10);
}
