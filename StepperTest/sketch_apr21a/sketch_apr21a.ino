void setup() {
  Serial.begin(115200);
  // put your setup code here, to run once:

}
String message;
void loop() {
  if (Serial.available()){
    message=Serial.readString();
    delay(3000);
    Serial.print("received:");
    Serial.println(message);
  }
  // put your main code here, to run repeatedly:

}
