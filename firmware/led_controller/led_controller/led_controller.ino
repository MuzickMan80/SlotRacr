/*
By default Arduino's analogWrite (and consequently pwmWrite() since it mimics analogWrite()) uses 8 bit 
pwm across all timers. 8 bit PWM allows for a total of 256 possible values. This library has some methods 
for fine tuning resolution if a higher resolution is needed:

void pwmWriteHR(uint8_t pin, uint16_t duty)
  Same a pwmWrite, except the range is 0 - 65535 (16 bit) instead 
  of 0 - 255 (8 bit)

float TimerX_GetResolution() (replace X with a timer number)
  Gets the timer's resolution in base 2. The value returned in other words 
  represents the number of bits required to represent the timer's range. ie 
  the value 7 means it takes 7 bits to represent all possible pin duties at 
  that frequency, or 7-bit resolution. Note that a float is returned, not 
  an int. 

float GetPinResolution(uint8_t pin)
  Returns the same value as TimerX_GetResolution(), but takes a pin number
  as a parameter so that the caller is timer agnostic.

There are several things to keep in mind when trying to optimize resolution:
 -pwmWriteHR() is only useful for 16 bit timers, since 8 bit timers are inherently limited to 8 bit pwm
 -The higher the frequency, the lower the resolution. pwmWriteHR() will automatically map input to the 
  actual timer resolution 
 -Resolution can be optimized in this way for 2 pins on the Uno (9 and 10), and 11 pins on the Mega (2, 
 3, 5, 6, 7, 8, 11, 12, 44, 45,  and 46)
  
Use the serial moniter to see output from this program
This example runs on mega and uno.
*/

#define countof(a) (sizeof(a)/sizeof(*a))

//use pin 11 on the mega for this example to work
int led = 13; // the pin that the LED is attached to

int lightPins[] = {
  2, 3, 4
};

void setup()
{
  Serial.begin(500000);
  Serial.println();

  pinMode(led, OUTPUT);
  digitalWrite(led, HIGH);

  for (int i = 0; i < countof(lightPins); ++i)
  {
    pinMode(lightPins[i], OUTPUT);
  }
}

bool writeOutputState(int output, int state)
{
  if (output < 0 || output >= countof(lightPins))
    return false;
  
  digitalWrite(lightPins[output], state ? HIGH : LOW);
  return true;
}

void runCommand(char* cmd)
{
  int32_t outNum;
  int32_t outState;
  bool ok=true;
  switch(cmd[0]) {

    case 'w':
      outNum = atol(strtok(cmd+1, ","));
      outState = atol(strtok(NULL, ","));
      ok=writeOutputState(outNum, outState);
      break;

    case 'i':
      Serial.println("LED");
      break;
      
    default:
      ok=0;
      break;
  }
  Serial.println(ok?"ok":"err");
  Serial.flush();
}

void processSerial()
{  
  const int maxInData = 30;
  static char inData[maxInData];
  static int inDataOffset = 0;
  static int toggle = LOW;
  
  if (Serial.available() > 0)
  {
    char received = Serial.read();
    inData[inDataOffset++] = received;

    if (received == '\n' || received == '\r' || inDataOffset == maxInData-1)
    {
      inData[inDataOffset] = 0;
      inDataOffset = 0;

      runCommand(inData);

      digitalWrite(led, toggle);
      toggle = !toggle;
    }
  }
}

void loop()
{
  processSerial();
}
