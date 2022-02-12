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

#define countof(a) (sizeof(a)/sizeof(*a))

//use pin 11 on the mega for this example to work
int led = 13; // the pin that the LED is attached to

/*
timer 0 (controls pin 13, 4);
timer 1 (controls pin 12, 11);
timer 2 (controls pin 10, 9);
timer 3 (controls pin 5, 3, 2);
timer 4 (controls pin 8, 7, 6);
Next revision, we should try to put each one on it's own timer, and avoid timer 0 which
is used for 
*/
int trackPins[] = {
  2, 3, 4, 5
};

int currentSensePins[] = {
  A3, A2, A1, A0
};

int buttonPins[] = {
  22, 23, 24, 25, 52, 53
};

int lightPins[] = {
  30, 31, 32, 33
};

int buzzerPins[] = {
  6, 7, 8, 9
};

int controlButtonPins[] = {
  52, 53
};

void setup()
{
  InitTimers(); //initialize all timers except for 0, to save time keeping functions
  Serial.begin(500000);
  Serial.println();

  pinMode(led, OUTPUT);
  digitalWrite(led, HIGH);

  for (int i = 0; i < countof(lightPins); ++i)
  {
    pinMode(lightPins[i], OUTPUT);
  }
  for (int i = 0; i < countof(trackPins); ++i)
  {
    pinMode(trackPins[i], OUTPUT);
  }
  for (int i = 0; i < countof(buzzerPins); ++i)
  {
    pinMode(buzzerPins[i], OUTPUT);
  }
  for (int i = 0; i < countof(buttonPins); ++i)
  {
    pinMode(buttonPins[i], INPUT_PULLUP);
  }
}

const int numButtons = countof(buttonPins);
int buttonStates[numButtons] = {0};
int buttonDelays[numButtons] = {0};

unsigned long lastButtonCheck = 0;
unsigned long buttonTickMs = 5;
unsigned int buttonDebounceTicks = 10;
unsigned int ticksPerMs = 6;
int test = 0;

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
          writeBuzzer(i,!state);
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
  if (lastButtonCheck++ > buttonTickMs*ticksPerMs)
  {
    lastButtonCheck = 0;
    updateButtonStates();
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

bool writeOutputState(int output, int state)
{
  if (output < 0 || output >= countof(lightPins))
    return false;
  
  digitalWrite(lightPins[output], state ? HIGH : LOW);
  return true;
}

bool writeOutputPower(int output, uint16_t power)
{
  if (output < 0 || output >= countof(trackPins))
    return false;
  
  pwmWriteHR(trackPins[output], power);
  return true;
}

bool writeOutputFreq(int freq)
{
  for (int lane = 0; lane < countof(trackPins); ++lane)
  {
    writeOutputPower(lane, 0);
    SetPinFrequency(trackPins[lane], freq);
  }
  
  return true;
}

bool writeBuzzer(int output, int on)
{
  if (output < 0 || output >= countof(buzzerPins))
    return false;
  
  digitalWrite(buzzerPins[output],on?HIGH:LOW);  
  return true;
}

int lastTrackPowerLane = 0;
int trackPowers[countof(currentSensePins)] = {0};
 
void updateTrackPowers()
{
  int trackPower = analogRead(currentSensePins[lastTrackPowerLane]);
  trackPowers[lastTrackPowerLane] = (trackPowers[lastTrackPowerLane] * 9 + trackPower) / 10;
  
  lastTrackPowerLane = (lastTrackPowerLane+1) % countof(currentSensePins);
  
  if (test == 2 && trackPowers[lastTrackPowerLane] > 30) 
  {
    Serial.print(lastTrackPowerLane);
    Serial.write(" : ");
    sendTrackPower(lastTrackPowerLane);
  }
}

bool sendTrackPower(int lane)
{
  if (lane < 0 || lane >= countof(currentSensePins))
    return false;
  
  Serial.println(trackPowers[lane]);
  return true;
}

bool sendTrackPowers()
{
  for (int lane = 0; lane < countof(currentSensePins); ++lane)
  {
    sendTrackPower(lane);
  }
  return true;
}

struct OutOfGasState
{
  bool enabled;
  int onTick;
  int offTick;
  uint16_t onPower;
  uint16_t offPower;
};

OutOfGasState oogStates[countof(trackPins)] = {{false,0,0,0,0}};
int oogTick = 0;
int oogPeriodMs = 170;
int oogPeriodTicks = oogPeriodMs*ticksPerMs;
const long powerMax = 65536L;

bool setOutOfGasPeriod(int periodMs)
{
  if (periodMs < 10 || periodMs > 500) {
    return false;
  }
  
  oogPeriodMs = periodMs;
  oogPeriodTicks = oogPeriodMs * ticksPerMs;

  for (int lane = 0; lane < countof(trackPins); ++lane)
  {
    stopOutOfGas(lane);
  }

  return true;
}

// car type 1:
// 120ms, 15k, 50k, 15k
// car type 2:
// 200ms, 15k, 65k, 30k
// car type 1:
// 200ms, 15k, 65k, 13k
// 170ms, 23k, 50k, 0k
bool startOutOfGas(int lane, int32_t duty, int32_t onPower, int32_t offPower)
{
  if (lane < 0 || lane >= countof(trackPins))
    return false;

  if (duty < 0 || duty > powerMax)
    return false;
  if (onPower < 0 || onPower > powerMax)
    return false;
  if (offPower < 0 || offPower > powerMax)
    return false;

  int onTime = duty * oogPeriodTicks / powerMax;
  int onTick = lane * oogPeriodTicks / countof(trackPins);
  int offTick = (onTick + onTime) % oogPeriodTicks;

  oogStates[lane].onTick = onTick;
  oogStates[lane].offTick = offTick;
  oogStates[lane].onPower = onPower;
  oogStates[lane].offPower = offPower;
  oogStates[lane].enabled = onTick != offTick;

  pwmWriteHR(trackPins[lane], 0);
  int startPower = onPower;
  if (onTick == offTick) {
    startPower = onTime == 0 ? offPower : onPower;
  }
  
  pwmWriteHR(trackPins[lane], startPower);
  
  return true;
}

bool stopOutOfGas(int lane)
{
  if (lane < 0 || lane >= countof(trackPins))
    return false;
    
  oogStates[lane].onTick = 0;
  oogStates[lane].offTick = 0;
  oogStates[lane].enabled = false;  
}

void runOutOfGas()
{
  oogTick = (oogTick + 1) % oogPeriodTicks;

  for (int lane = 0; lane < countof(trackPins); ++lane)
  {
    if (oogStates[lane].enabled)
    {
      if (oogStates[lane].onTick == oogTick)
      {
        pwmWriteHR(trackPins[lane], oogStates[lane].onPower);
      }
      else if (oogStates[lane].offTick == oogTick)
      {
        pwmWriteHR(trackPins[lane], oogStates[lane].offPower);
      }
    }
  }  
}

void runCommand(char* cmd)
{
  int pinStates;
  int32_t outNum;
  int32_t outFreq;
  int32_t outPower;
  int32_t onPower;
  int32_t idlePower;
  int32_t outState;
  bool ok=true;
  switch(cmd[0]) {
    case 'r':
      sendButtonStates();
      break;
    case 'w':
      outNum = atol(strtok(cmd+1, ","));
      outState = atol(strtok(NULL, ","));
      ok=writeOutputState(outNum, outState);
      break;
    case 'o':
      outNum = atol(strtok(cmd+1, ","));
      outPower = atol(strtok(NULL, ","));
      ok=writeOutputPower(outNum, outPower);
      break;
    case 'f':
      outFreq = atol(strtok(NULL, ","));
      ok=writeOutputFreq(outFreq);
      break;
    case 'b':
      outNum = atol(strtok(cmd+1, ","));
      outFreq = atol(strtok(NULL, ","));
      ok=writeBuzzer(outNum, outFreq);
      break;
    case 't':
      outState = atol(strtok(cmd+1, ","));
      test = outState;
      break;
    case 'p':
      outNum = atol(strtok(cmd+1, ","));
      ok=sendTrackPower(outNum);
      break;  
    case 'q':
      ok=sendTrackPowers();
      break;
    case 'g':
      outNum = atol(strtok(cmd+1, ","));
      outPower = atol(strtok(NULL, ","));
      onPower = atol(strtok(NULL, ","));
      idlePower = atol(strtok(NULL, ","));
      ok=startOutOfGas(outNum, outPower, onPower, idlePower);
      break;
    case 's':
      outFreq = atol(strtok(cmd+1, ","));
      ok=setOutOfGasPeriod(outFreq);
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

unsigned long lastLoopTime = 0;
int loopsInSec = 0;

void displayCyclesPerSecond()
{
  if ((millis() - lastLoopTime) < 1000)
  {
    loopsInSec++;
  }
  else
  {
    Serial.println(loopsInSec);
    loopsInSec = 0;
    lastLoopTime = millis();
  }
}

void loop()
{
  pollButtons();
  updateTrackPowers();
  runOutOfGas();
  processSerial();

  if (test == 2)
  {
    displayCyclesPerSecond();
  }
}
