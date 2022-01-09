EESchema Schematic File Version 4
EELAYER 30 0
EELAYER END
$Descr A4 11693 8268
encoding utf-8
Sheet 1 1
Title ""
Date ""
Rev ""
Comp ""
Comment1 ""
Comment2 ""
Comment3 ""
Comment4 ""
$EndDescr
$Comp
L Amplifier_Operational:MCP6004 U1
U 2 1 61D10B77
P 5550 1500
F 0 "U1" H 5550 1867 50  0000 C CNN
F 1 "MCP6004" H 5550 1776 50  0000 C CNN
F 2 "Package_DIP:DIP-14_W7.62mm" H 5500 1600 50  0001 C CNN
F 3 "http://ww1.microchip.com/downloads/en/DeviceDoc/21733j.pdf" H 5600 1700 50  0001 C CNN
	2    5550 1500
	1    0    0    -1  
$EndComp
$Comp
L Amplifier_Operational:MCP6004 U1
U 3 1 61D1237E
P 7600 1500
F 0 "U1" H 7600 1867 50  0000 C CNN
F 1 "MCP6004" H 7600 1776 50  0000 C CNN
F 2 "Package_DIP:DIP-14_W7.62mm" H 7550 1600 50  0001 C CNN
F 3 "http://ww1.microchip.com/downloads/en/DeviceDoc/21733j.pdf" H 7650 1700 50  0001 C CNN
	3    7600 1500
	1    0    0    -1  
$EndComp
$Comp
L Amplifier_Operational:MCP6004 U1
U 4 1 61D1296C
P 10100 1500
F 0 "U1" H 10100 1867 50  0000 C CNN
F 1 "MCP6004" H 10100 1776 50  0000 C CNN
F 2 "Package_DIP:DIP-14_W7.62mm" H 10050 1600 50  0001 C CNN
F 3 "http://ww1.microchip.com/downloads/en/DeviceDoc/21733j.pdf" H 10150 1700 50  0001 C CNN
	4    10100 1500
	1    0    0    -1  
$EndComp
$Comp
L Amplifier_Operational:MCP6004 U1
U 5 1 61D131E9
P 7000 5200
F 0 "U1" H 6958 5246 50  0000 L CNN
F 1 "MCP6004" H 6958 5155 50  0000 L CNN
F 2 "Package_DIP:DIP-14_W7.62mm" H 6950 5300 50  0001 C CNN
F 3 "http://ww1.microchip.com/downloads/en/DeviceDoc/21733j.pdf" H 7050 5400 50  0001 C CNN
	5    7000 5200
	1    0    0    -1  
$EndComp
$Comp
L power:+3V3 #PWR0101
U 1 1 61D13D33
P 6900 4750
F 0 "#PWR0101" H 6900 4600 50  0001 C CNN
F 1 "+3V3" H 6915 4923 50  0000 C CNN
F 2 "" H 6900 4750 50  0001 C CNN
F 3 "" H 6900 4750 50  0001 C CNN
	1    6900 4750
	1    0    0    -1  
$EndComp
$Comp
L power:GND #PWR0102
U 1 1 61D147D9
P 6900 5600
F 0 "#PWR0102" H 6900 5350 50  0001 C CNN
F 1 "GND" H 6905 5427 50  0000 C CNN
F 2 "" H 6900 5600 50  0001 C CNN
F 3 "" H 6900 5600 50  0001 C CNN
	1    6900 5600
	1    0    0    -1  
$EndComp
$Comp
L Device:R_US R4
U 1 1 61D15FB6
P 3200 1800
F 0 "R4" V 2995 1800 50  0000 C CNN
F 1 "10K" V 3086 1800 50  0000 C CNN
F 2 "Resistor_SMD:R_0603_1608Metric" V 3240 1790 50  0001 C CNN
F 3 "~" H 3200 1800 50  0001 C CNN
	1    3200 1800
	0    -1   -1   0   
$EndComp
$Comp
L Device:R_US R1
U 1 1 61D1C755
P 2000 1150
F 0 "R1" V 1795 1150 50  0000 C CNN
F 1 "100" V 1886 1150 50  0000 C CNN
F 2 "Resistor_SMD:R_0603_1608Metric" V 2040 1140 50  0001 C CNN
F 3 "~" H 2000 1150 50  0001 C CNN
	1    2000 1150
	0    1    1    0   
$EndComp
$Comp
L Device:R_US R2
U 1 1 61D1CF22
P 2500 1600
F 0 "R2" H 2568 1646 50  0000 L CNN
F 1 "0R01" H 2568 1555 50  0000 L CNN
F 2 "Resistor_SMD:R_2512_6332Metric" V 2540 1590 50  0001 C CNN
F 3 "~" H 2500 1600 50  0001 C CNN
	1    2500 1600
	-1   0    0    1   
$EndComp
Wire Wire Line
	2500 1450 2500 1400
Text Label 1500 1150 0    50   ~ 0
PWM0
Text Label 2700 850  2    50   ~ 0
OUT0
Text Label 3750 1500 2    50   ~ 0
A0
Wire Wire Line
	3500 1500 3550 1500
$Comp
L Transistor_FET:IRLZ34N Q1
U 1 1 61D1AA3C
P 2400 1150
F 0 "Q1" H 2604 1196 50  0000 L CNN
F 1 "IRLZ34N" H 2604 1105 50  0000 L CNN
F 2 "Package_TO_SOT_THT:TO-220-3_Vertical" H 2650 1075 50  0001 L CIN
F 3 "http://www.infineon.com/dgdl/irlz34npbf.pdf?fileId=5546d462533600a40153567206892720" H 2400 1150 50  0001 L CNN
	1    2400 1150
	1    0    0    -1  
$EndComp
Wire Wire Line
	2700 850  2500 850 
Wire Wire Line
	2500 850  2500 950 
$Comp
L Amplifier_Operational:MCP6004 U1
U 1 1 61D0F665
P 3200 1500
F 0 "U1" H 3200 1867 50  0000 C CNN
F 1 "MCP6004" H 3200 1776 50  0000 C CNN
F 2 "Package_DIP:DIP-14_W7.62mm" H 3150 1600 50  0001 C CNN
F 3 "http://ww1.microchip.com/downloads/en/DeviceDoc/21733j.pdf" H 3250 1700 50  0001 C CNN
	1    3200 1500
	1    0    0    -1  
$EndComp
$Comp
L power:GND #PWR0103
U 1 1 61D192D1
P 2850 2200
F 0 "#PWR0103" H 2850 1950 50  0001 C CNN
F 1 "GND" H 2855 2027 50  0000 C CNN
F 2 "" H 2850 2200 50  0001 C CNN
F 3 "" H 2850 2200 50  0001 C CNN
	1    2850 2200
	1    0    0    -1  
$EndComp
$Comp
L Device:R_US R3
U 1 1 61D17F61
P 2850 2000
F 0 "R3" H 2918 2046 50  0000 L CNN
F 1 "1.2K" H 2918 1955 50  0000 L CNN
F 2 "Resistor_SMD:R_0603_1608Metric" V 2890 1990 50  0001 C CNN
F 3 "~" H 2850 2000 50  0001 C CNN
	1    2850 2000
	1    0    0    -1  
$EndComp
Wire Wire Line
	2900 1600 2850 1600
Wire Wire Line
	2850 1600 2850 1800
Wire Wire Line
	2850 1800 3050 1800
Connection ~ 2850 1800
Wire Wire Line
	2850 1800 2850 1850
Wire Wire Line
	3550 1800 3550 1500
Wire Wire Line
	3350 1800 3550 1800
Connection ~ 3550 1500
Wire Wire Line
	3550 1500 3750 1500
Wire Wire Line
	2850 2200 2850 2150
Wire Wire Line
	2900 1400 2500 1400
Connection ~ 2500 1400
Wire Wire Line
	2500 1400 2500 1350
Wire Wire Line
	2500 1750 2500 2200
Wire Wire Line
	2500 2200 2850 2200
Connection ~ 2850 2200
Wire Wire Line
	2150 1150 2200 1150
Wire Wire Line
	1500 1150 1850 1150
$Comp
L Device:R_US R8
U 1 1 61D5E808
P 5550 1800
F 0 "R8" V 5345 1800 50  0000 C CNN
F 1 "10K" V 5436 1800 50  0000 C CNN
F 2 "Resistor_SMD:R_0603_1608Metric" V 5590 1790 50  0001 C CNN
F 3 "~" H 5550 1800 50  0001 C CNN
	1    5550 1800
	0    -1   -1   0   
$EndComp
$Comp
L Device:R_US R5
U 1 1 61D5E80E
P 4350 1150
F 0 "R5" V 4145 1150 50  0000 C CNN
F 1 "100" V 4236 1150 50  0000 C CNN
F 2 "Resistor_SMD:R_0603_1608Metric" V 4390 1140 50  0001 C CNN
F 3 "~" H 4350 1150 50  0001 C CNN
	1    4350 1150
	0    1    1    0   
$EndComp
$Comp
L Device:R_US R6
U 1 1 61D5E814
P 4850 1600
F 0 "R6" H 4918 1646 50  0000 L CNN
F 1 "0R01" H 4918 1555 50  0000 L CNN
F 2 "Resistor_SMD:R_2512_6332Metric" V 4890 1590 50  0001 C CNN
F 3 "~" H 4850 1600 50  0001 C CNN
	1    4850 1600
	-1   0    0    1   
$EndComp
Wire Wire Line
	4850 1450 4850 1400
Text Label 3850 1150 0    50   ~ 0
PWM1
Text Label 5050 850  2    50   ~ 0
OUT1
Text Label 6100 1500 2    50   ~ 0
A1
Wire Wire Line
	5850 1500 5900 1500
$Comp
L Transistor_FET:IRLZ34N Q2
U 1 1 61D5E81F
P 4750 1150
F 0 "Q2" H 4954 1196 50  0000 L CNN
F 1 "IRLZ34N" H 4954 1105 50  0000 L CNN
F 2 "Package_TO_SOT_THT:TO-220-3_Vertical" H 5000 1075 50  0001 L CIN
F 3 "http://www.infineon.com/dgdl/irlz34npbf.pdf?fileId=5546d462533600a40153567206892720" H 4750 1150 50  0001 L CNN
	1    4750 1150
	1    0    0    -1  
$EndComp
Wire Wire Line
	5050 850  4850 850 
Wire Wire Line
	4850 850  4850 950 
$Comp
L power:GND #PWR0104
U 1 1 61D5E82D
P 5200 2200
F 0 "#PWR0104" H 5200 1950 50  0001 C CNN
F 1 "GND" H 5205 2027 50  0000 C CNN
F 2 "" H 5200 2200 50  0001 C CNN
F 3 "" H 5200 2200 50  0001 C CNN
	1    5200 2200
	1    0    0    -1  
$EndComp
$Comp
L Device:R_US R7
U 1 1 61D5E833
P 5200 2000
F 0 "R7" H 5268 2046 50  0000 L CNN
F 1 "1.2K" H 5268 1955 50  0000 L CNN
F 2 "Resistor_SMD:R_0603_1608Metric" V 5240 1990 50  0001 C CNN
F 3 "~" H 5200 2000 50  0001 C CNN
	1    5200 2000
	1    0    0    -1  
$EndComp
Wire Wire Line
	5250 1600 5200 1600
Wire Wire Line
	5200 1600 5200 1800
Wire Wire Line
	5200 1800 5400 1800
Connection ~ 5200 1800
Wire Wire Line
	5200 1800 5200 1850
Wire Wire Line
	5900 1800 5900 1500
Wire Wire Line
	5700 1800 5900 1800
Connection ~ 5900 1500
Wire Wire Line
	5900 1500 6100 1500
Wire Wire Line
	5200 2200 5200 2150
Wire Wire Line
	5250 1400 4850 1400
Connection ~ 4850 1400
Wire Wire Line
	4850 1400 4850 1350
Wire Wire Line
	4850 1750 4850 2200
Wire Wire Line
	4850 2200 5200 2200
Connection ~ 5200 2200
Wire Wire Line
	4500 1150 4550 1150
Wire Wire Line
	3850 1150 4200 1150
$Comp
L Device:R_US R12
U 1 1 61D649D8
P 7600 1800
F 0 "R12" V 7395 1800 50  0000 C CNN
F 1 "10K" V 7486 1800 50  0000 C CNN
F 2 "Resistor_SMD:R_0603_1608Metric" V 7640 1790 50  0001 C CNN
F 3 "~" H 7600 1800 50  0001 C CNN
	1    7600 1800
	0    -1   -1   0   
$EndComp
$Comp
L Device:R_US R9
U 1 1 61D649DE
P 6400 1150
F 0 "R9" V 6195 1150 50  0000 C CNN
F 1 "100" V 6286 1150 50  0000 C CNN
F 2 "Resistor_SMD:R_0603_1608Metric" V 6440 1140 50  0001 C CNN
F 3 "~" H 6400 1150 50  0001 C CNN
	1    6400 1150
	0    1    1    0   
$EndComp
$Comp
L Device:R_US R10
U 1 1 61D649E4
P 6900 1600
F 0 "R10" H 6968 1646 50  0000 L CNN
F 1 "0R01" H 6968 1555 50  0000 L CNN
F 2 "Resistor_SMD:R_2512_6332Metric" V 6940 1590 50  0001 C CNN
F 3 "~" H 6900 1600 50  0001 C CNN
	1    6900 1600
	-1   0    0    1   
$EndComp
Wire Wire Line
	6900 1450 6900 1400
Text Label 5900 1150 0    50   ~ 0
PWM2
Text Label 7100 850  2    50   ~ 0
OUT2
Text Label 8150 1500 2    50   ~ 0
A2
Wire Wire Line
	7900 1500 7950 1500
$Comp
L Transistor_FET:IRLZ34N Q3
U 1 1 61D649EF
P 6800 1150
F 0 "Q3" H 7004 1196 50  0000 L CNN
F 1 "IRLZ34N" H 7004 1105 50  0000 L CNN
F 2 "Package_TO_SOT_THT:TO-220-3_Vertical" H 7050 1075 50  0001 L CIN
F 3 "http://www.infineon.com/dgdl/irlz34npbf.pdf?fileId=5546d462533600a40153567206892720" H 6800 1150 50  0001 L CNN
	1    6800 1150
	1    0    0    -1  
$EndComp
Wire Wire Line
	7100 850  6900 850 
Wire Wire Line
	6900 850  6900 950 
$Comp
L power:GND #PWR0105
U 1 1 61D649FD
P 7250 2200
F 0 "#PWR0105" H 7250 1950 50  0001 C CNN
F 1 "GND" H 7255 2027 50  0000 C CNN
F 2 "" H 7250 2200 50  0001 C CNN
F 3 "" H 7250 2200 50  0001 C CNN
	1    7250 2200
	1    0    0    -1  
$EndComp
$Comp
L Device:R_US R11
U 1 1 61D64A03
P 7250 2000
F 0 "R11" H 7318 2046 50  0000 L CNN
F 1 "1.2K" H 7318 1955 50  0000 L CNN
F 2 "Resistor_SMD:R_0603_1608Metric" V 7290 1990 50  0001 C CNN
F 3 "~" H 7250 2000 50  0001 C CNN
	1    7250 2000
	1    0    0    -1  
$EndComp
Wire Wire Line
	7300 1600 7250 1600
Wire Wire Line
	7250 1600 7250 1800
Wire Wire Line
	7250 1800 7450 1800
Connection ~ 7250 1800
Wire Wire Line
	7250 1800 7250 1850
Wire Wire Line
	7950 1800 7950 1500
Wire Wire Line
	7750 1800 7950 1800
Connection ~ 7950 1500
Wire Wire Line
	7950 1500 8150 1500
Wire Wire Line
	7250 2200 7250 2150
Wire Wire Line
	7300 1400 6900 1400
Connection ~ 6900 1400
Wire Wire Line
	6900 1400 6900 1350
Wire Wire Line
	6900 1750 6900 2200
Wire Wire Line
	6900 2200 7250 2200
Connection ~ 7250 2200
Wire Wire Line
	6550 1150 6600 1150
Wire Wire Line
	5900 1150 6250 1150
$Comp
L Device:R_US R16
U 1 1 61D70927
P 10100 1800
F 0 "R16" V 9895 1800 50  0000 C CNN
F 1 "10K" V 9986 1800 50  0000 C CNN
F 2 "Resistor_SMD:R_0603_1608Metric" V 10140 1790 50  0001 C CNN
F 3 "~" H 10100 1800 50  0001 C CNN
	1    10100 1800
	0    -1   -1   0   
$EndComp
$Comp
L Device:R_US R13
U 1 1 61D7092D
P 8900 1150
F 0 "R13" V 8695 1150 50  0000 C CNN
F 1 "100" V 8786 1150 50  0000 C CNN
F 2 "Resistor_SMD:R_0603_1608Metric" V 8940 1140 50  0001 C CNN
F 3 "~" H 8900 1150 50  0001 C CNN
	1    8900 1150
	0    1    1    0   
$EndComp
$Comp
L Device:R_US R14
U 1 1 61D70933
P 9400 1600
F 0 "R14" H 9468 1646 50  0000 L CNN
F 1 "0R01" H 9468 1555 50  0000 L CNN
F 2 "Resistor_SMD:R_2512_6332Metric" V 9440 1590 50  0001 C CNN
F 3 "~" H 9400 1600 50  0001 C CNN
	1    9400 1600
	-1   0    0    1   
$EndComp
Wire Wire Line
	9400 1450 9400 1400
Text Label 8400 1150 0    50   ~ 0
PWM3
Text Label 9600 850  2    50   ~ 0
OUT3
Text Label 10650 1500 2    50   ~ 0
A3
Wire Wire Line
	10400 1500 10450 1500
$Comp
L Transistor_FET:IRLZ34N Q4
U 1 1 61D7093E
P 9300 1150
F 0 "Q4" H 9504 1196 50  0000 L CNN
F 1 "IRLZ34N" H 9504 1105 50  0000 L CNN
F 2 "Package_TO_SOT_THT:TO-220-3_Vertical" H 9550 1075 50  0001 L CIN
F 3 "http://www.infineon.com/dgdl/irlz34npbf.pdf?fileId=5546d462533600a40153567206892720" H 9300 1150 50  0001 L CNN
	1    9300 1150
	1    0    0    -1  
$EndComp
Wire Wire Line
	9600 850  9400 850 
Wire Wire Line
	9400 850  9400 950 
$Comp
L power:GND #PWR0106
U 1 1 61D7094C
P 9750 2200
F 0 "#PWR0106" H 9750 1950 50  0001 C CNN
F 1 "GND" H 9755 2027 50  0000 C CNN
F 2 "" H 9750 2200 50  0001 C CNN
F 3 "" H 9750 2200 50  0001 C CNN
	1    9750 2200
	1    0    0    -1  
$EndComp
$Comp
L Device:R_US R15
U 1 1 61D70952
P 9750 2000
F 0 "R15" H 9818 2046 50  0000 L CNN
F 1 "1.2K" H 9818 1955 50  0000 L CNN
F 2 "Resistor_SMD:R_0603_1608Metric" V 9790 1990 50  0001 C CNN
F 3 "~" H 9750 2000 50  0001 C CNN
	1    9750 2000
	1    0    0    -1  
$EndComp
Wire Wire Line
	9800 1600 9750 1600
Wire Wire Line
	9750 1600 9750 1800
Wire Wire Line
	9750 1800 9950 1800
Connection ~ 9750 1800
Wire Wire Line
	9750 1800 9750 1850
Wire Wire Line
	10450 1800 10450 1500
Wire Wire Line
	10250 1800 10450 1800
Connection ~ 10450 1500
Wire Wire Line
	10450 1500 10650 1500
Wire Wire Line
	9750 2200 9750 2150
Wire Wire Line
	9800 1400 9400 1400
Connection ~ 9400 1400
Wire Wire Line
	9400 1400 9400 1350
Wire Wire Line
	9400 1750 9400 2200
Wire Wire Line
	9400 2200 9750 2200
Connection ~ 9750 2200
Wire Wire Line
	9050 1150 9100 1150
Wire Wire Line
	8400 1150 8750 1150
Wire Wire Line
	6900 4750 6900 4900
Wire Wire Line
	6900 5500 6900 5600
$Comp
L MCU_Module:Arduino_UNO_R3 A1
U 1 1 61D934F9
P 2300 3900
F 0 "A1" H 2300 5081 50  0000 C CNN
F 1 "Arduino_UNO_R3" H 2300 4990 50  0000 C CNN
F 2 "Module:Arduino_UNO_R3_WithMountingHoles" H 2300 3900 50  0001 C CIN
F 3 "https://www.arduino.cc/en/Main/arduinoBoardUno" H 2300 3900 50  0001 C CNN
	1    2300 3900
	1    0    0    -1  
$EndComp
Text Label 1350 3500 0    50   ~ 0
PWM0
Text Label 1350 3600 0    50   ~ 0
PWM1
Text Label 1350 3700 0    50   ~ 0
PWM2
Text Label 1350 3800 0    50   ~ 0
PWM3
Text Label 3000 3900 2    50   ~ 0
A0
Text Label 3000 4000 2    50   ~ 0
A1
Text Label 3000 4100 2    50   ~ 0
A2
Text Label 3000 4200 2    50   ~ 0
A3
$Comp
L power:+3V3 #PWR0107
U 1 1 61D96AD6
P 2400 2700
F 0 "#PWR0107" H 2400 2550 50  0001 C CNN
F 1 "+3V3" H 2415 2873 50  0000 C CNN
F 2 "" H 2400 2700 50  0001 C CNN
F 3 "" H 2400 2700 50  0001 C CNN
	1    2400 2700
	1    0    0    -1  
$EndComp
Wire Wire Line
	2400 2700 2400 2900
Wire Wire Line
	1350 3500 1800 3500
Wire Wire Line
	1350 3600 1800 3600
Wire Wire Line
	1350 3700 1800 3700
Wire Wire Line
	1350 3800 1800 3800
Wire Wire Line
	2800 3900 3000 3900
Wire Wire Line
	2800 4000 3000 4000
Wire Wire Line
	2800 4100 3000 4100
Wire Wire Line
	2800 4200 3000 4200
$Comp
L power:GND #PWR0108
U 1 1 61DA81DC
P 2300 5150
F 0 "#PWR0108" H 2300 4900 50  0001 C CNN
F 1 "GND" H 2305 4977 50  0000 C CNN
F 2 "" H 2300 5150 50  0001 C CNN
F 3 "" H 2300 5150 50  0001 C CNN
	1    2300 5150
	1    0    0    -1  
$EndComp
Wire Wire Line
	2300 5150 2300 5100
Wire Wire Line
	2400 5000 2400 5100
Wire Wire Line
	2400 5100 2300 5100
Connection ~ 2300 5100
Wire Wire Line
	2300 5100 2300 5000
Wire Wire Line
	2200 5000 2200 5100
Wire Wire Line
	2200 5100 2300 5100
$EndSCHEMATC
