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

#include <PWM.h>

//use pin 11 on the mega for this example to work
int led = 13; // the pin that the LED is attached to

int pwmPins[] = {
  2, 3, 4, 5,
  6, 7, 8, 9
};

int analogPins[] = {
  A0, A1, A2, A3,
  A4, A5, A6, A7
};

int buttonPins[] = {
  23, 25, 27, 29,
  31, 33, 35, 37
};

#define countof(a) (sizeof(a)/sizeof(*a))
const int numButtons = countof(buttonPins);
int buttonStates[numButtons] = {0};
int buttonDelays[numButtons] = {0};

int lightPins[] = {
  22, 24, 26, 28,
  30, 32, 34, 36
};

unsigned long lastButtonCheck = 0;
unsigned long buttonTickMs = 5;
unsigned int buttonDebounceTicks = 10;
bool test = false;

void updateButtonStates()
{
  for (int i = 0; i < numButtons; ++i)
  {
    int lastState = buttonStates[i];
    int state = digitalRead(buttonPins[i]);
    int buttonDelay = buttonDelays[i];

    if (state != lastState)
    {
      if (buttonDelay < buttonDebounceTicks)
      {
        buttonDelays[i]++;
      }
      else
      {        
        buttonStates[i] = state;
        buttonDelays[i] = 0;

        if(test) {
          writeOutputState(i,!state);
          writeOutputPower(i,state ? 0:60000);
        }
      }
    }
    else
    {
      buttonDelays[i] = 0;
    }
  }
}

void pollButtons()
{
  if ((millis() - lastButtonCheck) > buttonTickMs)
  {
    lastButtonCheck = millis();
    updateButtonStates();
  }
}

void setup()
{
  InitTimersSafe(); //initialize all timers except for 0, to save time keeping functions
  Serial.begin(500000);
  Serial.println();

  pinMode(led, OUTPUT);
  digitalWrite(led, HIGH);

  for (int i = 0; i < countof(lightPins); ++i)
  {
    pinMode(lightPins[i], OUTPUT);
  }
  for (int i = 0; i < countof(pwmPins); ++i)
  {
    pinMode(pwmPins[i], OUTPUT);
  }
  for (int i = 0; i < countof(buttonPins); ++i)
  {
    pinMode(buttonPins[i], INPUT_PULLUP);
  }
}

void sendButtonStates()
{
  for (int i = 0; i < numButtons; ++i)
  {
    Serial.write(buttonStates[i] ? '0' : '1');
  }
  Serial.println();
}

void writeOutputState(int output, int state)
{
  if (output < countof(lightPins))
  {
    digitalWrite(lightPins[output], state ? HIGH : LOW);
  }
}

void writeOutputPower(int output, int power)
{
  if (output < countof(pwmPins))
  {
    pwmWriteHR(pwmPins[output], power);
  }
}

void writeOutputFreq(int output, int freq)
{
  if (output < countof(pwmPins))
  {
    SetPinFrequency(pwmPins[output], freq);
  }
}

void runCommand(char* cmd)
{
  int pinStates;
  int outNum;
  int outFreq;
  int outPower;
  int outState;
  int ok=1;
  switch(cmd[0]) {
    case 'p':
      break;
    case 'r':
      sendButtonStates();
      break;
    case 'w':
      outNum = atoi(strtok(cmd+1, ","));
      outState = atoi(strtok(NULL, ","));
      writeOutputState(outNum, outState);
      break;
    case 'o':
      outNum = atoi(strtok(cmd+1, ","));
      outPower = atoi(strtok(NULL, ","));
      writeOutputPower(outNum, outPower);
      break;
    case 'f':
      outNum = atoi(strtok(cmd+1, ","));
      outFreq = atoi(strtok(NULL, ","));
      writeOutputFreq(outNum, outFreq);
      break;
    case 't':
      outState = atoi(strtok(cmd+1, ","));
      test = !!outState;
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
int trackPower = 0;
unsigned long lastTrackRead = 0;

void loop()
{
  pollButtons();
  processSerial();
/*
  trackPower = (trackPower * 30 + analogRead(A0))/31;
  if ((millis() - lastTrackRead) > 500) {
    Serial.println(5 * (trackPower/1024.0));
    lastTrackRead = millis();
  }
*/
}
