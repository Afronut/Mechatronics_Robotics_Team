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
Adafruit_DCMotor *rightMotor = AFMS.getMotor(3);
// You can also make another motor on port M2
Adafruit_DCMotor *leftMotor = AFMS.getMotor(4);

int forkliftPosition = 40; //Defines the initial state (height) of the forklift. There are 6 states total
int forklift1 = 0;         //These are the different levels, 1->4
int forklift2 = 10;
int qrlevel1 = 40; // this is the appropriate height to read a qr code on level 1
int forklift3 = 600;
int forklift4 = 610;
int qrlevel2 = 650; // this is the appropriate height to read a qr code on level 2

String command;

int rPin = A2;       //input pin from the IR reader
int lPin = A3;       //input pin from the IR reader
int rsensorVal = 0;  //initializes the value being read from the sensor
int lsensorVal = 0;  //initializes the value being read from the sensor
int turningVal1 = 0; //sets a turning value to compare the sensorValue to so it knows to turn left or right
int turningVal2 = 0;
int threshold = 500; //this is the threshold value being checked against sensorVal

void setup()
{
  // Serial.begin(115200);  // BAUD RATE FOR RASPBERRY PI
  Serial.begin(115200);
  Serial.println("Main Roomba Code!");
  pinMode(rPin, INPUT);
  pinMode(lPin, INPUT);

  AFMS.begin(); // create with the default frequency 1.6KHz
  //AFMS.begin(1000);  // OR with a different frequency, say 1KHz

  stepperMotor->setSpeed(10); // 10 rpm

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

void loop()
{

  if (Serial.available())
  {
//    Serial.println("received"); //if a serial port is available, send a message back to the pi
//    delay(2000);
    command = Serial.readString(); //stores the pi message
    delay(2000);
//    Serial.println(command);
//    delay(2);
  }
  Serial.print(command);
  if (command == "line")
  {
    sensorRead(); //calls the line follower function
  }

  else if (command == "up")
  {
    stepperUp();
  }
  else if (command == "down")
  {
    stepperDown();
  }

  else if (command == "turn_left")
  {
    goLeft();
  }

  else if (command == "turn_right")
  {
    goRight();
  }

  else if (command == "go_straight")
  {
    goStraight();
  }

  else if (command == "check_pallets")
  {
    bool codeScanResult;
    forkliftPosition = setStepperLocation(forkliftPosition); //function checking if the forklift is in the bottom level location or fixes it
    Serial.print("The forklift location is: ");
    Serial.println(forkliftPosition);
    codeScanResult = stepperScan(forkliftPosition); //Start the scanning process for pallets
    while (codeScanResult == false)
    {
      Serial.println("Restarting the search for the pallet code");
      Serial.print("The forklift level is: ");
      Serial.println(forkliftPosition);
      delay(3000);
      forkliftPosition = setStepperLocation(forkliftPosition);
      codeScanResult = stepperScan(forkliftPosition);
    }
  }

  else if (command == "turn_left_90")
  {
    goLeft90();
    stopMotors();
  }

  else if (command == "stop")
  {
    rightMotor->run(RELEASE);
    leftMotor->run(RELEASE);
    delay(10000);
  }

  //  stepperUp();
  //  delay(2000);
  //  stepperDown();
  //  delay(2000);
}

void sensorRead()
{
  lsensorVal = analogRead(lPin);
  rsensorVal = analogRead(rPin);
  Serial.print(lsensorVal);
  Serial.print("    ");
  Serial.println(rsensorVal);
  delay(1000);

  if (rsensorVal > threshold && lsensorVal > threshold)
  {
    goStraight();
  }

  else if (rsensorVal < threshold)
  {
    goLeft();
  }
  else if (lsensorVal < threshold)
  {
    goRight();
  }
}

void goStraight()
{
  // Drive both
  Serial.println("Straight");
  rightMotor->run(FORWARD);
  rightMotor->setSpeed(70);
  leftMotor->run(FORWARD);
  leftMotor->setSpeed(70);
  delay(2000);
}

void goLeft()
{
  Serial.println("Left");
  rightMotor->run(FORWARD);
  rightMotor->setSpeed(200);
  leftMotor->run(FORWARD);
  leftMotor->setSpeed(0);
  delay(2000);
  Serial.println("Left");
}

void goRight()
{
  Serial.println("Right");
  rightMotor->run(FORWARD);
  rightMotor->setSpeed(0);
  leftMotor->run(FORWARD);
  leftMotor->setSpeed(200);
  delay(2000);
  Serial.println("Right");
}

int setStepperLocation(int actual)
{
  int changedDistance;
  Serial.print("The state is: ");
  Serial.println(actual);
  if (qrlevel1 == actual)
  {
    Serial.println("The forklift is already at qr level 1");
    return actual;
  }
  else
  {
    Serial.println("Stepper moving forklift to level 1");
    changedDistance = actual - qrlevel1;
    Serial.print("Actual: ");
    Serial.println(actual);
    Serial.print("distance back to level 1: ");
    Serial.println(changedDistance);
    if (changedDistance > 0)
    {
      stepperMotor->step(changedDistance, BACKWARD, DOUBLE);
      actual = qrlevel1;
    }
    else
    {
      stepperMotor->step(changedDistance, FORWARD, DOUBLE);
      actual = qrlevel1;
    }
    return actual;
  }
}

bool stepperScan(int forkLocation)
{
  String palletScanResult;        //String that will be received whether or not pallet QR code was found
  String forkliftExtensionResult; //String that will be received when the forklift is extended
  Serial.write("scan for pallet code");
  delay(3000);
  palletScanResult = Serial.readString();
  if (palletScanResult == "pallet code found")
  {
    setForkliftPickupLevel(); //gets the pallet in the right position
    Serial.write("extend forklift");
    Serial.println("The correct pallet was found!");
    forkliftExtensionResult = Serial.readString();
    if (forkliftExtensionResult.substring(0) == "forklift extended")
    {
      palletPickup(); //starts the pallet pickup sequence
      forkliftPosition = forkLocation;
      return true;
    }
  }
  else
  {
    Serial.println("The pallet wasn't found. Moving to qr level 2");
    stepperMotor->step(qrlevel2 - qrlevel1, FORWARD, DOUBLE);
    forkliftPosition = forklift3;
    return false;
  }
}

void setForkliftPickupLevel()
{
  if (forkliftPosition == qrlevel1)
  {
    // move from qrlevel1 to forklift1
    stepperMotor->step(qrlevel1 - forklift1, BACKWARD, DOUBLE);
  }
  if (forkliftPosition == qrlevel2)
  {
    stepperMotor->step(qrlevel2 - forklift3, BACKWARD, DOUBLE);
  }
  else
  {
    Serial.println("The forklift is not located at either qr level 1 or qr level 2. Fix code");
  }
}

void palletPickup()
{
  Serial.println("Picking up pallet");
  stepperMotor->step(forklift3 - forklift1, FORWARD, DOUBLE);
}

// JUST FOR TESTING. NOT IN MAIN SCRIPT
void stepperDown()
{
  stepperMotor->step(400, FORWARD, DOUBLE);
  Serial.println("Stepper Down");
}

// JUST FOR TESTING. NOT IN MAIN SCRIPT
void stepperUp()
{
  stepperMotor->step(400, BACKWARD, DOUBLE);
  Serial.print("Stepper Up");
}

// FUNCTION FOR A 90 DEGREE LEFT TURN
void goLeft90()
{
  Serial.println("Left 90");
  rightMotor->run(FORWARD);
  rightMotor->setSpeed(150);
  leftMotor->run(BACKWARD);
  leftMotor->setSpeed(150);
  delay(2000);
  Serial.println("Left");
}

// FUNCTION FOR A 90 DEGREE RIGHT TURN
void goRight90()
{
  Serial.println("Right 90");
  rightMotor->run(FORWARD);
  rightMotor->setSpeed(0);
  leftMotor->run(FORWARD);
  leftMotor->setSpeed(70);
  delay(2000);
  Serial.println("Right");
}

void stopMotors()
{
  rightMotor->run(RELEASE);
  leftMotor->run(RELEASE);
  command = "stop\n";
  Serial.println();
  Serial.print("The new command is: ");
  Serial.print(command.substring(0));
  delay(5000);
}
