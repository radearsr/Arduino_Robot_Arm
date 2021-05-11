#include <Servo.h>

Servo servoPemutar;
Servo servoLenganBawah;
Servo servoLenganAtas;
Servo servoPencapit;

int servoPositions[4];

void setup() {
  Serial.begin(9600);
  servoPemutar.attach(8);
  servoLenganBawah.attach(9);
  servoLenganAtas.attach(10);
  servoPencapit.attach(11);
}

void loop() {
  while(Serial.available()){
    String input = Serial.readStringUntil('\n');
    servoPositions[0] = input.substring(0,3).toInt();
    servoPositions[1] = input.substring(3,6).toInt();
    servoPositions[2] = input.substring(6,9).toInt();
    servoPositions[3] = input.substring(9,12).toInt();
  }

  servoPemutar.write(servoPositions[0]);
  servoLenganBawah.write(servoPositions[1]);
  servoLenganAtas.write(servoPositions[2]);
  servoPencapit.write(servoPositions[3]);
  
  delay(500);
}
