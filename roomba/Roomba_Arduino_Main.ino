/* 
This is a test sketch for the Adafruit assembled Motor Shield for Arduino v2
It won't work with v1.x motor shields! Only for the v2's with built in PWM
control

For use with the Adafruit Motor Shield v2 
---->	http://www.adafruit.com/products/1438
*/


#include <Wire.h>
#include <Adafruit_MotorShield.h>

// Create the motor shield object with the default I2C address
Adafruit_MotorShield AFMS = Adafruit_MotorShield(); 
// Or, create it with a different I2C address (say for stacking)
// Adafruit_MotorShield AFMS = Adafruit_MotorShield(0x61); 

// Connect a stepper motor with 200 steps per revolution (1.8 degree)
// to motor port #2 (M3 and M4)
Adafruit_StepperMotor *stepperMotor = AFMS.getStepper(200, 1);
// Select which 'port' M1, M2, M3 or M4. In this case, M1
Adafruit_DCMotor *rightMotor = AFMS.getMotor(1);
// You can also make another motor on port M2
Adafruit_DCMotor *leftMotor = AFMS.getMotor(2);

int stepperLocation1 = 1; //Defines the initial state (height) of the forklift. There are 4 states total

int rPin = A0; //input pin from the IR reader
int lPin = A1; //input pin from the IR reader
int rsensorVal = 0;  //initializes the value being read from the sensor
int lsensorVal = 0;  //initializes the value being read from the sensor
int turningVal1 = 0; //sets a turning value to compare the sensorValue to so it knows to turn left or right
int turningVal2 = 0;
int threshold = 1000; //this is the threshold value being checked against sensorVal

void setup() {
  Serial.begin(9600);           // set up Serial library at 9600 bps
  Serial.println("Main Roomba Code!");
  pinMode(rPin, INPUT);
  pinMode(lPin, INPUT);


  AFMS.begin();  // create with the default frequency 1.6KHz
  //AFMS.begin(1000);  // OR with a different frequency, say 1KHz
  
  stepperMotor->setSpeed(10);  // 10 rpm 
  
  // Set the speed to start
  rightMotor->setSpeed(150);
  rightMotor->run(FORWARD);
  // turn on motor
  rightMotor->run(RELEASE);

  leftMotor->setSpeed(150);
  leftMotor->run(FORWARD);
  // turn on motor
  leftMotor->run(RELEASE);  
}

void loop() {
  String command;
  if (Serial.available()){
    Serial.print("received"); //if a serial port is available, send a message back to the pi
    command  = Serial.readString(); //stores the pi message
  }
  if (command == "line") {
    sensorRead(); //calls the line follower function
  }
    
  if (command == "up") {
    stepperUp();
  }
  if (command == "down") {
    stepperDown();
  } 

  if (command == "check pallets") {
    int stepperTarget = 1; //sets the target state to level 1 to start scanning
    setStepperLocation1(stepperTarget,stepperLocation); //function checking if the forklift is in the correct location or fixes it
    
  }

//  stepperUp();
//  delay(2000);
//  stepperDown();
//  delay(2000);
}

void sensorRead() {
  lsensorVal = analogRead(lPin);
  rsensorVal = analogRead(rPin);
  Serial.print(lsensorVal);
  Serial.print("    ");
  Serial.println(rsensorVal);
  delay(1000);

  if(rsensorVal > threshold && lsensorVal > threshold)
  {
  goStraight();
  }

  else if (rsensorVal < threshold)
  {
    goLeft();
  }
  else if (lsensorVal < threshold){
    goRight();
  }
}

void goStraight()
{
  // Drive both
 Serial.println("Straight");
 rightMotor->run(FORWARD);
 rightMotor->setSpeed(255);
 leftMotor->run(FORWARD); 
 leftMotor->setSpeed(100);   
 delay(2000);
} 

void goLeft(){
 Serial.println("Left");
 rightMotor->run(FORWARD);
 rightMotor->setSpeed(255);
 leftMotor->run(FORWARD);
 leftMotor->setSpeed(0);   
 delay(2000);
  Serial.println("Left");
}

void goRight(){
 Serial.println("Right");
 rightMotor->run(FORWARD);
 rightMotor->setSpeed(0);
 leftMotor->run(FORWARD); 
 leftMotor->setSpeed(255);   
 delay(2000);
 Serial.println("Right");
}

void setStepperLocation1(target,actual) {
  if (target == actual) {
    return true;
  }
  else if (actual == 2) {
    Serial.println("Stepper Level 2 to 1");
    stepperMotor->step(10,FORWARD,DOUBLE);
  }
  else if (actual == 3 {
    Serial.println("Stepper Level 3 to 1");
    stepperMotor->step(300,FORWARD,DOUBLE);
  }
  else if (actual == 4) {
    Serial.println("Stepper Level 4 to 1");
    stepperMotor->step(400,FORWARD,DOUBLE)
  }
}

void stepperDown()
{
  stepperMotor->step(400, FORWARD, DOUBLE); 
  Serial.println("Stepper Down");
}

void stepperUp()
{
  stepperMotor->step(400, BACKWARD, DOUBLE);
  Serial.print("Stepper Up");
}
