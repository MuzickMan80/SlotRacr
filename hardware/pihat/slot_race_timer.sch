EESchema Schematic File Version 4
EELAYER 30 0
EELAYER END
$Descr A3 16535 11693
encoding utf-8
Sheet 1 1
Title "Raspberry Pi HAT"
Date ""
Rev "A"
Comp ""
Comment1 ""
Comment2 ""
Comment3 ""
Comment4 ""
$EndDescr
$Comp
L Mechanical:MountingHole H1
U 1 1 5834BC4A
P 5200 2200
F 0 "H1" H 5050 2300 60  0000 C CNN
F 1 "3mm_Mounting_Hole" H 5200 2050 60  0000 C CNN
F 2 "project_footprints:NPTH_3mm_ID" H 5100 2200 60  0001 C CNN
F 3 "" H 5100 2200 60  0001 C CNN
	1    5200 2200
	1    0    0    -1  
$EndComp
$Comp
L Mechanical:MountingHole H2
U 1 1 5834BCDF
P 6200 2200
F 0 "H2" H 6050 2300 60  0000 C CNN
F 1 "3mm_Mounting_Hole" H 6200 2050 60  0000 C CNN
F 2 "project_footprints:NPTH_3mm_ID" H 6100 2200 60  0001 C CNN
F 3 "" H 6100 2200 60  0001 C CNN
	1    6200 2200
	1    0    0    -1  
$EndComp
$Comp
L Mechanical:MountingHole H3
U 1 1 5834BD62
P 5200 2750
F 0 "H3" H 5050 2850 60  0000 C CNN
F 1 "3mm_Mounting_Hole" H 5200 2600 60  0000 C CNN
F 2 "project_footprints:NPTH_3mm_ID" H 5100 2750 60  0001 C CNN
F 3 "" H 5100 2750 60  0001 C CNN
	1    5200 2750
	1    0    0    -1  
$EndComp
$Comp
L Mechanical:MountingHole H4
U 1 1 5834BDED
P 6250 2750
F 0 "H4" H 6100 2850 60  0000 C CNN
F 1 "3mm_Mounting_Hole" H 6250 2600 60  0000 C CNN
F 2 "project_footprints:NPTH_3mm_ID" H 6150 2750 60  0001 C CNN
F 3 "" H 6150 2750 60  0001 C CNN
	1    6250 2750
	1    0    0    -1  
$EndComp
$Comp
L raspberrypi_hat:OX40HAT J3
U 1 1 58DFC771
P 2600 2250
F 0 "J3" H 2950 2350 50  0000 C CNN
F 1 "40HAT" H 2300 2350 50  0000 C CNN
F 2 "Connector_PinSocket_2.54mm:PinSocket_2x20_P2.54mm_Vertical" H 2600 2450 50  0001 C CNN
F 3 "" H 1900 2250 50  0000 C CNN
	1    2600 2250
	1    0    0    -1  
$EndComp
Text Notes 4850 1900 0    118  ~ 24
Mounting Holes
Text Notes 1650 2000 0    118  ~ 24
40-Pin HAT Connector
Text Label 800  4150 0    60   ~ 0
GND
Wire Wire Line
	2000 4150 800  4150
Text Label 800  3450 0    60   ~ 0
GND
Wire Wire Line
	2000 3450 800  3450
Text Label 800  2650 0    60   ~ 0
GND
Wire Wire Line
	2000 2650 800  2650
Text Label 800  2250 0    60   ~ 0
P3V3_HAT
Wire Wire Line
	2000 2250 800  2250
Wire Wire Line
	3200 2850 4400 2850
Wire Wire Line
	3200 3150 4400 3150
Wire Wire Line
	3200 3650 4400 3650
Wire Wire Line
	3200 3850 4400 3850
Text Label 4400 2850 2    60   ~ 0
GND
Text Label 4400 3150 2    60   ~ 0
GND
Text Label 4400 3650 2    60   ~ 0
GND
Text Label 4400 3850 2    60   ~ 0
GND
Text Label 4400 2450 2    60   ~ 0
GND
Wire Wire Line
	3200 2450 4400 2450
Text Label 4400 2350 2    60   ~ 0
P5V_HAT
Wire Wire Line
	3200 2350 4400 2350
Text Label 4400 2250 2    60   ~ 0
P5V_HAT
Wire Wire Line
	3200 2250 4400 2250
Text Notes 850  1250 0    100  ~ 0
This is based on the official Raspberry Pi spec to be able to call an extension board a HAT.\nhttps://github.com/raspberrypi/hats/blob/master/designguide.md
$Comp
L Connector:Screw_Terminal_01x09 J1
U 1 1 618A8266
P 7750 2250
F 0 "J1" H 7830 2292 50  0000 L CNN
F 1 "Screw_Terminal_01x09" H 7830 2201 50  0000 L CNN
F 2 "Connector_Phoenix_MSTB:PhoenixContact_MSTBA_2,5_9-G-5,08_1x09_P5.08mm_Horizontal" H 7750 2250 50  0001 C CNN
F 3 "~" H 7750 2250 50  0001 C CNN
	1    7750 2250
	1    0    0    -1  
$EndComp
$Comp
L Connector:Screw_Terminal_01x02 J2
U 1 1 618A954D
P 7750 3100
F 0 "J2" H 7830 3092 50  0000 L CNN
F 1 "Screw_Terminal_01x02" H 7830 3001 50  0000 L CNN
F 2 "Connector_Phoenix_MSTB:PhoenixContact_MSTBA_2,5_2-G-5,08_1x02_P5.08mm_Horizontal" H 7750 3100 50  0001 C CNN
F 3 "~" H 7750 3100 50  0001 C CNN
	1    7750 3100
	1    0    0    -1  
$EndComp
$Comp
L Device:R_POT_US RV1
U 1 1 618A9E4D
P 6150 4250
F 0 "RV1" H 6082 4296 50  0000 R CNN
F 1 "10k" H 6082 4205 50  0000 R CNN
F 2 "Potentiometer_THT:Potentiometer_Bourns_3339P_Vertical" H 6150 4250 50  0001 C CNN
F 3 "~" H 6150 4250 50  0001 C CNN
	1    6150 4250
	1    0    0    -1  
$EndComp
$Comp
L Device:R_Small_US R1
U 1 1 618AEB01
P 6150 4650
F 0 "R1" H 6218 4696 50  0000 L CNN
F 1 "1k" H 6218 4605 50  0000 L CNN
F 2 "Resistor_THT:R_Axial_DIN0204_L3.6mm_D1.6mm_P2.54mm_Vertical" H 6150 4650 50  0001 C CNN
F 3 "~" H 6150 4650 50  0001 C CNN
	1    6150 4650
	1    0    0    -1  
$EndComp
$Comp
L Device:R_Small_US R3
U 1 1 618B088E
P 6450 4100
F 0 "R3" H 6518 4146 50  0000 L CNN
F 1 "100" H 6518 4055 50  0000 L CNN
F 2 "Resistor_THT:R_Axial_DIN0204_L3.6mm_D1.6mm_P2.54mm_Vertical" H 6450 4100 50  0001 C CNN
F 3 "~" H 6450 4100 50  0001 C CNN
	1    6450 4100
	1    0    0    -1  
$EndComp
$Comp
L power:GND #PWR01
U 1 1 618B842E
P 6150 4750
F 0 "#PWR01" H 6150 4500 50  0001 C CNN
F 1 "GND" H 6155 4577 50  0000 C CNN
F 2 "" H 6150 4750 50  0001 C CNN
F 3 "" H 6150 4750 50  0001 C CNN
	1    6150 4750
	1    0    0    -1  
$EndComp
Wire Wire Line
	6150 4400 6150 4550
Wire Wire Line
	6300 4250 6350 4250
Wire Wire Line
	6450 4250 6450 4200
Wire Wire Line
	6450 3850 6300 3850
Wire Wire Line
	6450 3850 6450 4000
Wire Wire Line
	6350 4450 6350 4250
Connection ~ 6350 4250
Wire Wire Line
	6350 4250 6450 4250
$Comp
L Device:R_POT_US RV3
U 1 1 618C0068
P 7050 4250
F 0 "RV3" H 6982 4296 50  0000 R CNN
F 1 "10k" H 6982 4205 50  0000 R CNN
F 2 "Potentiometer_THT:Potentiometer_Bourns_3339P_Vertical" H 7050 4250 50  0001 C CNN
F 3 "~" H 7050 4250 50  0001 C CNN
	1    7050 4250
	1    0    0    -1  
$EndComp
$Comp
L Device:R_Small_US R5
U 1 1 618C006E
P 7050 4650
F 0 "R5" H 7118 4696 50  0000 L CNN
F 1 "1k" H 7118 4605 50  0000 L CNN
F 2 "Resistor_THT:R_Axial_DIN0204_L3.6mm_D1.6mm_P2.54mm_Vertical" H 7050 4650 50  0001 C CNN
F 3 "~" H 7050 4650 50  0001 C CNN
	1    7050 4650
	1    0    0    -1  
$EndComp
$Comp
L Device:R_Small_US R7
U 1 1 618C0074
P 7350 4100
F 0 "R7" H 7418 4146 50  0000 L CNN
F 1 "100" H 7418 4055 50  0000 L CNN
F 2 "Resistor_THT:R_Axial_DIN0204_L3.6mm_D1.6mm_P2.54mm_Vertical" H 7350 4100 50  0001 C CNN
F 3 "~" H 7350 4100 50  0001 C CNN
	1    7350 4100
	1    0    0    -1  
$EndComp
$Comp
L power:GND #PWR03
U 1 1 618C007A
P 7050 4750
F 0 "#PWR03" H 7050 4500 50  0001 C CNN
F 1 "GND" H 7055 4577 50  0000 C CNN
F 2 "" H 7050 4750 50  0001 C CNN
F 3 "" H 7050 4750 50  0001 C CNN
	1    7050 4750
	1    0    0    -1  
$EndComp
Wire Wire Line
	7050 4400 7050 4550
Wire Wire Line
	7200 4250 7250 4250
Wire Wire Line
	7350 4250 7350 4200
Wire Wire Line
	7350 3850 7200 3850
Wire Wire Line
	7350 3850 7350 4000
Wire Wire Line
	7250 4450 7250 4250
Connection ~ 7250 4250
Wire Wire Line
	7250 4250 7350 4250
$Comp
L Device:R_POT_US RV2
U 1 1 618C1B5E
P 6200 5600
F 0 "RV2" H 6132 5646 50  0000 R CNN
F 1 "10k" H 6132 5555 50  0000 R CNN
F 2 "Potentiometer_THT:Potentiometer_Bourns_3339P_Vertical" H 6200 5600 50  0001 C CNN
F 3 "~" H 6200 5600 50  0001 C CNN
	1    6200 5600
	1    0    0    -1  
$EndComp
$Comp
L Device:R_Small_US R2
U 1 1 618C1B64
P 6200 6000
F 0 "R2" H 6268 6046 50  0000 L CNN
F 1 "1k" H 6268 5955 50  0000 L CNN
F 2 "Resistor_THT:R_Axial_DIN0204_L3.6mm_D1.6mm_P2.54mm_Vertical" H 6200 6000 50  0001 C CNN
F 3 "~" H 6200 6000 50  0001 C CNN
	1    6200 6000
	1    0    0    -1  
$EndComp
$Comp
L Device:R_Small_US R4
U 1 1 618C1B6A
P 6500 5450
F 0 "R4" H 6568 5496 50  0000 L CNN
F 1 "100" H 6568 5405 50  0000 L CNN
F 2 "Resistor_THT:R_Axial_DIN0204_L3.6mm_D1.6mm_P2.54mm_Vertical" H 6500 5450 50  0001 C CNN
F 3 "~" H 6500 5450 50  0001 C CNN
	1    6500 5450
	1    0    0    -1  
$EndComp
$Comp
L power:GND #PWR02
U 1 1 618C1B70
P 6200 6100
F 0 "#PWR02" H 6200 5850 50  0001 C CNN
F 1 "GND" H 6205 5927 50  0000 C CNN
F 2 "" H 6200 6100 50  0001 C CNN
F 3 "" H 6200 6100 50  0001 C CNN
	1    6200 6100
	1    0    0    -1  
$EndComp
Wire Wire Line
	6200 5750 6200 5900
Wire Wire Line
	6350 5600 6400 5600
Wire Wire Line
	6500 5600 6500 5550
Wire Wire Line
	6500 5200 6350 5200
Wire Wire Line
	6500 5200 6500 5350
Wire Wire Line
	6400 5800 6400 5600
Connection ~ 6400 5600
Wire Wire Line
	6400 5600 6500 5600
$Comp
L Device:R_POT_US RV4
U 1 1 618C3584
P 7050 5600
F 0 "RV4" H 6982 5646 50  0000 R CNN
F 1 "10k" H 6982 5555 50  0000 R CNN
F 2 "Potentiometer_THT:Potentiometer_Bourns_3339P_Vertical" H 7050 5600 50  0001 C CNN
F 3 "~" H 7050 5600 50  0001 C CNN
	1    7050 5600
	1    0    0    -1  
$EndComp
$Comp
L Device:R_Small_US R6
U 1 1 618C358A
P 7050 6000
F 0 "R6" H 7118 6046 50  0000 L CNN
F 1 "1k" H 7118 5955 50  0000 L CNN
F 2 "Resistor_THT:R_Axial_DIN0204_L3.6mm_D1.6mm_P2.54mm_Vertical" H 7050 6000 50  0001 C CNN
F 3 "~" H 7050 6000 50  0001 C CNN
	1    7050 6000
	1    0    0    -1  
$EndComp
$Comp
L Device:R_Small_US R8
U 1 1 618C3590
P 7350 5450
F 0 "R8" H 7418 5496 50  0000 L CNN
F 1 "100" H 7418 5405 50  0000 L CNN
F 2 "Resistor_THT:R_Axial_DIN0204_L3.6mm_D1.6mm_P2.54mm_Vertical" H 7350 5450 50  0001 C CNN
F 3 "~" H 7350 5450 50  0001 C CNN
	1    7350 5450
	1    0    0    -1  
$EndComp
$Comp
L power:GND #PWR04
U 1 1 618C3596
P 7050 6100
F 0 "#PWR04" H 7050 5850 50  0001 C CNN
F 1 "GND" H 7055 5927 50  0000 C CNN
F 2 "" H 7050 6100 50  0001 C CNN
F 3 "" H 7050 6100 50  0001 C CNN
	1    7050 6100
	1    0    0    -1  
$EndComp
Wire Wire Line
	7050 5750 7050 5900
Wire Wire Line
	7200 5600 7250 5600
Wire Wire Line
	7350 5600 7350 5550
Wire Wire Line
	7350 5200 7200 5200
Wire Wire Line
	7350 5200 7350 5350
Wire Wire Line
	7250 5800 7250 5600
Connection ~ 7250 5600
Wire Wire Line
	7250 5600 7350 5600
$Comp
L Device:R_POT_US RV5
U 1 1 618CAAA2
P 7800 4250
F 0 "RV5" H 7732 4296 50  0000 R CNN
F 1 "10k" H 7732 4205 50  0000 R CNN
F 2 "Potentiometer_THT:Potentiometer_Bourns_3339P_Vertical" H 7800 4250 50  0001 C CNN
F 3 "~" H 7800 4250 50  0001 C CNN
	1    7800 4250
	1    0    0    -1  
$EndComp
$Comp
L Device:R_Small_US R9
U 1 1 618CAAA8
P 7800 4650
F 0 "R9" H 7868 4696 50  0000 L CNN
F 1 "1k" H 7868 4605 50  0000 L CNN
F 2 "Resistor_THT:R_Axial_DIN0204_L3.6mm_D1.6mm_P2.54mm_Vertical" H 7800 4650 50  0001 C CNN
F 3 "~" H 7800 4650 50  0001 C CNN
	1    7800 4650
	1    0    0    -1  
$EndComp
$Comp
L Device:R_Small_US R11
U 1 1 618CAAAE
P 8100 4100
F 0 "R11" H 8168 4146 50  0000 L CNN
F 1 "100" H 8168 4055 50  0000 L CNN
F 2 "Resistor_THT:R_Axial_DIN0204_L3.6mm_D1.6mm_P2.54mm_Vertical" H 8100 4100 50  0001 C CNN
F 3 "~" H 8100 4100 50  0001 C CNN
	1    8100 4100
	1    0    0    -1  
$EndComp
$Comp
L power:GND #PWR05
U 1 1 618CAAB4
P 7800 4750
F 0 "#PWR05" H 7800 4500 50  0001 C CNN
F 1 "GND" H 7805 4577 50  0000 C CNN
F 2 "" H 7800 4750 50  0001 C CNN
F 3 "" H 7800 4750 50  0001 C CNN
	1    7800 4750
	1    0    0    -1  
$EndComp
Wire Wire Line
	7800 4400 7800 4550
Wire Wire Line
	7950 4250 8000 4250
Wire Wire Line
	8100 4250 8100 4200
Wire Wire Line
	8100 3850 7950 3850
Wire Wire Line
	8100 3850 8100 4000
Wire Wire Line
	8000 4450 8000 4250
Connection ~ 8000 4250
Wire Wire Line
	8000 4250 8100 4250
$Comp
L Device:R_POT_US RV7
U 1 1 618CAAC5
P 8700 4250
F 0 "RV7" H 8632 4296 50  0000 R CNN
F 1 "10k" H 8632 4205 50  0000 R CNN
F 2 "Potentiometer_THT:Potentiometer_Bourns_3339P_Vertical" H 8700 4250 50  0001 C CNN
F 3 "~" H 8700 4250 50  0001 C CNN
	1    8700 4250
	1    0    0    -1  
$EndComp
$Comp
L Device:R_Small_US R13
U 1 1 618CAACB
P 8700 4650
F 0 "R13" H 8768 4696 50  0000 L CNN
F 1 "1k" H 8768 4605 50  0000 L CNN
F 2 "Resistor_THT:R_Axial_DIN0204_L3.6mm_D1.6mm_P2.54mm_Vertical" H 8700 4650 50  0001 C CNN
F 3 "~" H 8700 4650 50  0001 C CNN
	1    8700 4650
	1    0    0    -1  
$EndComp
$Comp
L Device:R_Small_US R15
U 1 1 618CAAD1
P 9000 4100
F 0 "R15" H 9068 4146 50  0000 L CNN
F 1 "100" H 9068 4055 50  0000 L CNN
F 2 "Resistor_THT:R_Axial_DIN0204_L3.6mm_D1.6mm_P2.54mm_Vertical" H 9000 4100 50  0001 C CNN
F 3 "~" H 9000 4100 50  0001 C CNN
	1    9000 4100
	1    0    0    -1  
$EndComp
$Comp
L power:GND #PWR07
U 1 1 618CAAD7
P 8700 4750
F 0 "#PWR07" H 8700 4500 50  0001 C CNN
F 1 "GND" H 8705 4577 50  0000 C CNN
F 2 "" H 8700 4750 50  0001 C CNN
F 3 "" H 8700 4750 50  0001 C CNN
	1    8700 4750
	1    0    0    -1  
$EndComp
Wire Wire Line
	8700 4400 8700 4550
Wire Wire Line
	8850 4250 8900 4250
Wire Wire Line
	9000 4250 9000 4200
Wire Wire Line
	9000 3850 8850 3850
Wire Wire Line
	9000 3850 9000 4000
Wire Wire Line
	8900 4450 8900 4250
Connection ~ 8900 4250
Wire Wire Line
	8900 4250 9000 4250
$Comp
L Device:R_POT_US RV6
U 1 1 618CAAE8
P 7850 5600
F 0 "RV6" H 7782 5646 50  0000 R CNN
F 1 "10k" H 7782 5555 50  0000 R CNN
F 2 "Potentiometer_THT:Potentiometer_Bourns_3339P_Vertical" H 7850 5600 50  0001 C CNN
F 3 "~" H 7850 5600 50  0001 C CNN
	1    7850 5600
	1    0    0    -1  
$EndComp
$Comp
L Device:R_Small_US R10
U 1 1 618CAAEE
P 7850 6000
F 0 "R10" H 7918 6046 50  0000 L CNN
F 1 "1k" H 7918 5955 50  0000 L CNN
F 2 "Resistor_THT:R_Axial_DIN0204_L3.6mm_D1.6mm_P2.54mm_Vertical" H 7850 6000 50  0001 C CNN
F 3 "~" H 7850 6000 50  0001 C CNN
	1    7850 6000
	1    0    0    -1  
$EndComp
$Comp
L Device:R_Small_US R12
U 1 1 618CAAF4
P 8150 5450
F 0 "R12" H 8218 5496 50  0000 L CNN
F 1 "100" H 8218 5405 50  0000 L CNN
F 2 "Resistor_THT:R_Axial_DIN0204_L3.6mm_D1.6mm_P2.54mm_Vertical" H 8150 5450 50  0001 C CNN
F 3 "~" H 8150 5450 50  0001 C CNN
	1    8150 5450
	1    0    0    -1  
$EndComp
$Comp
L power:GND #PWR06
U 1 1 618CAAFA
P 7850 6100
F 0 "#PWR06" H 7850 5850 50  0001 C CNN
F 1 "GND" H 7855 5927 50  0000 C CNN
F 2 "" H 7850 6100 50  0001 C CNN
F 3 "" H 7850 6100 50  0001 C CNN
	1    7850 6100
	1    0    0    -1  
$EndComp
Wire Wire Line
	7850 5750 7850 5900
Wire Wire Line
	8000 5600 8050 5600
Wire Wire Line
	8150 5600 8150 5550
Wire Wire Line
	8150 5200 8000 5200
Wire Wire Line
	8150 5200 8150 5350
Wire Wire Line
	8050 5800 8050 5600
Connection ~ 8050 5600
Wire Wire Line
	8050 5600 8150 5600
$Comp
L Device:R_POT_US RV8
U 1 1 618CAB0B
P 8700 5600
F 0 "RV8" H 8632 5646 50  0000 R CNN
F 1 "10k" H 8632 5555 50  0000 R CNN
F 2 "Potentiometer_THT:Potentiometer_Bourns_3339P_Vertical" H 8700 5600 50  0001 C CNN
F 3 "~" H 8700 5600 50  0001 C CNN
	1    8700 5600
	1    0    0    -1  
$EndComp
$Comp
L Device:R_Small_US R14
U 1 1 618CAB11
P 8700 6000
F 0 "R14" H 8768 6046 50  0000 L CNN
F 1 "1k" H 8768 5955 50  0000 L CNN
F 2 "Resistor_THT:R_Axial_DIN0204_L3.6mm_D1.6mm_P2.54mm_Vertical" H 8700 6000 50  0001 C CNN
F 3 "~" H 8700 6000 50  0001 C CNN
	1    8700 6000
	1    0    0    -1  
$EndComp
$Comp
L Device:R_Small_US R16
U 1 1 618CAB17
P 9000 5450
F 0 "R16" H 9068 5496 50  0000 L CNN
F 1 "100" H 9068 5405 50  0000 L CNN
F 2 "Resistor_THT:R_Axial_DIN0204_L3.6mm_D1.6mm_P2.54mm_Vertical" H 9000 5450 50  0001 C CNN
F 3 "~" H 9000 5450 50  0001 C CNN
	1    9000 5450
	1    0    0    -1  
$EndComp
$Comp
L power:GND #PWR08
U 1 1 618CAB1D
P 8700 6100
F 0 "#PWR08" H 8700 5850 50  0001 C CNN
F 1 "GND" H 8705 5927 50  0000 C CNN
F 2 "" H 8700 6100 50  0001 C CNN
F 3 "" H 8700 6100 50  0001 C CNN
	1    8700 6100
	1    0    0    -1  
$EndComp
Wire Wire Line
	8700 5750 8700 5900
Wire Wire Line
	8850 5600 8900 5600
Wire Wire Line
	9000 5600 9000 5550
Wire Wire Line
	9000 5200 8850 5200
Wire Wire Line
	9000 5200 9000 5350
Wire Wire Line
	8900 5800 8900 5600
Connection ~ 8900 5600
Wire Wire Line
	8900 5600 9000 5600
Text Label 7100 1850 0    50   ~ 0
P3V3_HAT
Wire Wire Line
	7100 1850 7550 1850
Wire Wire Line
	7100 1950 7550 1950
Wire Wire Line
	7100 2050 7550 2050
Wire Wire Line
	7100 2150 7550 2150
Wire Wire Line
	7100 2250 7550 2250
Wire Wire Line
	7100 2350 7550 2350
Wire Wire Line
	7100 2450 7550 2450
Wire Wire Line
	7100 2550 7550 2550
Wire Wire Line
	7100 2650 7550 2650
Wire Wire Line
	7100 3100 7550 3100
Wire Wire Line
	7100 3200 7550 3200
Text Label 7250 1950 2    50   ~ 0
IN0
Text Label 7250 2050 2    50   ~ 0
IN1
Text Label 7250 2150 2    50   ~ 0
IN2
Text Label 7250 2250 2    50   ~ 0
IN3
Text Label 7250 2350 2    50   ~ 0
IN4
Text Label 7250 2450 2    50   ~ 0
IN5
Text Label 7250 2550 2    50   ~ 0
IN6
Text Label 7250 2650 2    50   ~ 0
IN7
Text Label 6500 4450 2    50   ~ 0
IN0
Wire Wire Line
	6350 4450 6500 4450
Text Label 7400 4450 2    50   ~ 0
IN1
Text Label 8150 4450 2    50   ~ 0
IN2
Text Label 9050 4450 2    50   ~ 0
IN3
Wire Wire Line
	8900 4450 9050 4450
Wire Wire Line
	8000 4450 8150 4450
Wire Wire Line
	7250 4450 7400 4450
Text Label 6550 5800 2    50   ~ 0
IN4
Wire Wire Line
	6400 5800 6550 5800
Text Label 7400 5800 2    50   ~ 0
IN5
Wire Wire Line
	7250 5800 7400 5800
Text Label 8200 5800 2    50   ~ 0
IN6
Wire Wire Line
	8050 5800 8200 5800
Text Label 9050 5800 2    50   ~ 0
IN7
Wire Wire Line
	8900 5800 9050 5800
Text Label 800  3750 0    50   ~ 0
TRIG4
Text Label 800  3850 0    50   ~ 0
TRIG5
Text Label 800  3950 0    50   ~ 0
TRIG6
Text Label 800  2950 0    50   ~ 0
TRIG2
Wire Wire Line
	800  3750 2000 3750
Wire Wire Line
	800  3850 2000 3850
Wire Wire Line
	800  3950 2000 3950
Wire Wire Line
	800  2950 2000 2950
Text Label 800  2850 0    50   ~ 0
TRIG1
Wire Wire Line
	800  2850 2000 2850
Text Label 800  2750 0    50   ~ 0
TRIG0
Wire Wire Line
	800  2750 2000 2750
Text Label 800  2550 0    50   ~ 0
RESET
Text Label 800  4050 0    50   ~ 0
TRIG7
Wire Wire Line
	800  4050 2000 4050
Wire Wire Line
	800  2550 2000 2550
Text Label 800  3650 0    50   ~ 0
TRIG3
Wire Wire Line
	800  3650 2000 3650
Text Label 7100 3100 0    50   ~ 0
RESET
Text Label 7100 3200 0    50   ~ 0
GND
Text Label 6300 3850 0    50   ~ 0
TRIG0
Text Label 7200 3850 0    50   ~ 0
TRIG1
Text Label 7950 3850 0    50   ~ 0
TRIG2
Text Label 8850 3850 0    50   ~ 0
TRIG3
Text Label 6350 5200 0    50   ~ 0
TRIG4
Text Label 7200 5200 0    50   ~ 0
TRIG5
Text Label 8000 5200 0    50   ~ 0
TRIG6
Text Label 8850 5200 0    50   ~ 0
TRIG7
$EndSCHEMATC
