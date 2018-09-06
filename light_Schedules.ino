  /*
  Lighting schedules
  Growth stage     Hours of light      Hours of darkness
  Seedling         16-24               8-0
  Clone            18-24               6-0
  Vegetative       18                  6
  Flowering        12                  12

  Watering time
  
  */
const int in1 = 5; //digital 5 pin
const int in2 = 6; //digital 6 pin

void setup() {
  // put your setup code here, to run once:
  pinMode(in1, OUTPUT);
  digitalWrite(in1, HIGH);
  pinMode(in2, OUTPUT);
  digitalWrite(in2, HIGH);
}

void loop() {
  // put your main code here, to run repeatedly:


  //Test
  //On
  digitalWrite(in1, HIGH);
  digitalWrite(in2, HIGH);
  delay(10000); // 5s
  //Off
  digitalWrite(in1, LOW);
  digitalWrite(in2, LOW);
  delay(10000); // 3s

  /* 
  loop to put the light cycles in for watering
  
  for(int i = 0, i = 7, i++){
    if(i )
    }
    */
    
  /*
  //SEEDLING
  //On
  digitalWrite(in1, HIGH);
  delay(57600000); // 16hrs
  //Off
  digitalWrite(in1, LOW);
  delay(28800000); // 8hrs
  */

  /*
  //CLONE
  //On
  digitalWrite(in1, HIGH);
  delay(64800000); // 18hrs
  //Off
  digitalWrite(in1, LOW);
  delay(21600000); // 6hrs
  */

  /*
  //VEGETATIVE
  //On
  digitalWrite(in1, HIGH);
  delay(64800000); // 18hrs
  //Off
  digitalWrite(in1, LOW);
  delay(21600000); // 6hrs
  */

  /*
  //FLOWERING
  //On
  digitalWrite(in1, HIGH);
  delay(43200000); // 12hrs
  //Off
  digitalWrite(in1, LOW);
  delay(43200000); // 12hrs
  */
}
