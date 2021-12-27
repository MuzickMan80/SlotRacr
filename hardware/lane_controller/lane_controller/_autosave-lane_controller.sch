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
L Relay:JW2 RL?
U 1 1 61BECE2E
P 4050 3100
F 0 "RL?" H 3421 3054 50  0000 R CNN
F 1 "JW2" H 3421 3145 50  0000 R CNN
F 2 "Relay_THT:Relay_DPDT_Panasonic_JW2" H 4700 3050 50  0001 L CNN
F 3 "http://www3.panasonic.biz/ac/e_download/control/relay/power/catalog/mech_eng_jw.pdf?via=ok" H 4050 3100 50  0001 C CNN
	1    4050 3100
	1    0    0    1   
$EndComp
$Comp
L Relay:RAYEX-L90 K?
U 1 1 61BEDC00
P 3250 4500
F 0 "K?" H 3680 4546 50  0000 L CNN
F 1 "RAYEX-L90" H 3680 4455 50  0000 L CNN
F 2 "Relay_THT:Relay_SPDT_RAYEX-L90" H 3700 4450 50  0001 L CNN
F 3 "https://a3.sofastcdn.com/attachment/7jioKBjnRiiSrjrjknRiwS77gwbf3zmp/L90-SERIES.pdf" H 3600 5500 50  0001 L CNN
	1    3250 4500
	1    0    0    -1  
$EndComp
$Comp
L Relay:RAYEX-L90 K?
U 1 1 61BEEB1D
P 3550 5850
F 0 "K?" H 3120 5804 50  0000 R CNN
F 1 "RAYEX-L90" H 3120 5895 50  0000 R CNN
F 2 "Relay_THT:Relay_SPDT_RAYEX-L90" H 4000 5800 50  0001 L CNN
F 3 "https://a3.sofastcdn.com/attachment/7jioKBjnRiiSrjrjknRiwS77gwbf3zmp/L90-SERIES.pdf" H 3900 6850 50  0001 L CNN
	1    3550 5850
	1    0    0    1   
$EndComp
$Comp
L power:+12V #PWR?
U 1 1 61BEF5D8
P 2550 6550
F 0 "#PWR?" H 2550 6400 50  0001 C CNN
F 1 "+12V" H 2565 6723 50  0000 C CNN
F 2 "" H 2550 6550 50  0001 C CNN
F 3 "" H 2550 6550 50  0001 C CNN
	1    2550 6550
	1    0    0    -1  
$EndComp
$Comp
L power:+9V #PWR?
U 1 1 61BEFF3B
P 2250 6750
F 0 "#PWR?" H 2250 6600 50  0001 C CNN
F 1 "+9V" H 2265 6923 50  0000 C CNN
F 2 "" H 2250 6750 50  0001 C CNN
F 3 "" H 2250 6750 50  0001 C CNN
	1    2250 6750
	1    0    0    -1  
$EndComp
$Comp
L power:GND #PWR?
U 1 1 61BF05FC
P 5050 6750
F 0 "#PWR?" H 5050 6500 50  0001 C CNN
F 1 "GND" H 5055 6577 50  0000 C CNN
F 2 "" H 5050 6750 50  0001 C CNN
F 3 "" H 5050 6750 50  0001 C CNN
	1    5050 6750
	1    0    0    -1  
$EndComp
Wire Wire Line
	2550 6550 3250 6550
Wire Wire Line
	3250 6550 3250 6250
Wire Wire Line
	2250 6750 3450 6750
Wire Wire Line
	3450 6750 3450 6250
Wire Wire Line
	3350 5450 3350 4900
Wire Wire Line
	3350 4900 3450 4900
Wire Wire Line
	3350 4100 3350 3650
Wire Wire Line
	3350 3400 3550 3400
Wire Wire Line
	3350 3650 4150 3650
Wire Wire Line
	4150 3650 4150 3400
Connection ~ 3350 3650
Wire Wire Line
	3350 3650 3350 3400
Wire Wire Line
	5050 6750 5050 3900
Wire Wire Line
	5050 3900 3950 3900
Wire Wire Line
	3750 3400 3950 3400
Connection ~ 3950 3400
Wire Wire Line
	3950 3400 3950 3900
$EndSCHEMATC
