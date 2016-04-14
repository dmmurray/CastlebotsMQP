/* Encoder Library - Basic Example
 * http://www.pjrc.com/teensy/td_libs_Encoder.html
 * This example code is in the public domain.
 *
 * Modified by Corey on 4/11
 *
 * Notes:
 *    requires Arduino Uno pins 2, 3, 4, and 5
 *    whichever encoder is designated Encoder 1 will have its distance flipped
 *        --if this needs to be changed, look to first line of encoders()
 */
 
#include <Encoder.h>

// Change these two numbers to the pins connected to your encoder.
//   Best Performance: both pins have interrupt capability
//   Good Performance: only the first pin has interrupt capability
//   Low Performance:  neither pin has interrupt capability

// Arduino Uno pins 2 and 3 should have interrupt capability
Encoder enc1(2, 4);
Encoder enc2(3, 5);
//   avoid using pins with LEDs attached
//   on Arduino Uno, that should be just pin 13

long oldPosition1  = -999;
long oldPosition2  = -999;
int distance1 = 0;
int distance2 = 0; 

int heading = 1;
int tmp_heading;

byte directions[3];

/****************************************************************************************************/

//Set up motor pins: only use digital pins (PWM functionality not enabled with DRV8833)  

const int leftMotorForward = 6; //
const int leftMotorBackward = 9; //

const int rightMotorForward = 10; //
const int rightMotorBackward = 11; //

//Disactivate print statements during runtme unless necessary for Pi communication 
boolean DEBUG = false;

//To store commands from Pi and current position (cm)
int destination [2];
int currentPosition [2];

//calculate the distance for wheels to turn to make 90 degree turn; 7.5 cm is distance between wheels

float turningArcLength = 90*(7.5/2)*(3.14/180);

//set up interrupt pin
const byte interruptPin = 2;

/****************************************************************************************************/

void setup(){
  
  Serial.begin(9600);
  
  if (DEBUG == true){
    Serial.println("Encoder Setup Complete"); 
  } 

  //Set up motor pins
  pinMode(leftMotorForward, OUTPUT);
  pinMode(leftMotorBackward, OUTPUT);
  pinMode(rightMotorForward, OUTPUT);
  pinMode(rightMotorBackward, OUTPUT);

  //Default: motors are off to prevent surprises
  stopMotor(leftMotorForward);
  stopMotor(leftMotorForward);
  stopMotor(leftMotorForward);
  stopMotor(leftMotorForward);
  
  if (DEBUG == true){
    Serial.println("Pin Setup Complete");
  }

  pinMode(intrruptPin, INPUT_PULLUP);
  //attachInterrupt(digitalPinToInterrupt(interru
  
}

void loop(){

}

//read from encoders and convert to distance in cm
void encoders() {
  
  long newPosition1 = 0 - enc1.read();
  long newPosition2 = enc2.read();
  int newPosition1, newPosition2;
  if (newPosition1 != oldPosition1 || newPosition2 != oldPosition2) {
    oldPosition1 = newPosition1;
    oldPosition2 = newPosition2;
    
    distance1 = calcDist(newPosition1);
    distance2 = calcDist(newPosition2);
    
    //Serial.print(distance1);
    //Serial.println(" cm for Encoder 1");
    //Serial.print(distance2);
    //Serial.println(" cm for Encoder 2");
  }
}  

//convert ticks to centimeters
int calcDist(long encVal) {
  float cm_value = encVal / 250.7;
  //int sol = value;
  return cm_value;
}

//Send current position to RasPi
void sendPosition(){
  for(int i=0; i<3; i++){
    Serial.println(currentPosition[i]);
  }
}

void drive(int motorpin){
  analogWrite(motorpin, HIGH);
}

void turnLeft(){
  while((distance1 - distance2 == 0) && abs(distance1) <= turningArcLength){
    drive(leftMotorBackward);
    drive(rightMotorForward);
  }
  tmp_heading = heading - 1;
  if(tmp_heading != 0){
    heading = tmp % 4;
  }
  else{
    heading = 4;
  }
}

void turnRight(){
  
  while((distance1 + distance2 == 0) && abs(distance1) <= turningArcLength){
    drive(leftMotorForward);
    drive(rightMotorBackward);
  }
  tmp_heading = heading + 1;
  if(tmp_heading != 0){
    heading = tmp % 4;
  }
  else{
    heading = 4;    
  }
}

void stopMotor(int motorpin){
  digitalWrite(motorpin, LOW);
}

void readDirections(){
  if (Serial.available()){
    for(int i=0; i<4; i++){
      directions[i] = Serial.readBytes;
      i++;
    }
  }
}

void execute(){
  if (directions[0] != null){
    destination_heading = directions[0];
    destination_distance = (10*directions[1])+(directions[2]);
  }
  
  int currentHeading = heading;
  int headingToGo = directions[0] - currentHeading;
 
  if(headingToGo != 0 && headingToGo > 1){
    for(int k = 0; k < headingToGo; k++){
      turnLeft();
    }
  }
  else{
    turnRight();
  }
}

// TODO turn to face north
// TODO array buffer for destination
// TODO switch-case between encoders, driving, serial comm 

//Serial - receieve 1 3-byte string where 1st byte is heading and next two are distance to travel

  
