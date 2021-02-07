Materials:
1 x Raspberry Pi Zero WH ($14) [https://www.adafruit.com/product/3708]
1 x Mini HDMI to HDMI Cable ($6) [https://www.adafruit.com/product/2775]
1 x 5v 2.5a supply ($8) [https://www.adafruit.com/product/1995]
1 x NOOBS SD Card ($15) [https://www.adafruit.com/product/4266]
4 x Photo Transistor ($4) [https://www.adafruit.com/product/2831]
4 x 100ohm Resistor ($1)

4 x 10kohm Resistor ($1)

F to M jumper wires ($2) [https://www.adafruit.com/product/1954]
1 x Breadboard ($5) [https://www.adafruit.com/product/64]

1 x HDMI Display ($42) [https://www.amazon.com/Yasoca-Inch-Monitor-HDMI-Raspberry/dp/B089YSHMYS/ref=sr_1_19?dchild=1&keywords=hdmi%2Bdisplay%2B7%2Binch&qid=1612496742&refinements=p_85%3A2470955011&rnid=2470954011&rps=1&sr=8-19&th=1]
Total: $93

Steps:
1. Enable ZeroConf networking [https://learn.adafruit.com/bonjour-zeroconf-networking-for-windows-and-linux]
2. Install VSCode 

from [https://wolfgang-ziegler.com/blog/setting-up-a-raspberrypi-in-kiosk-mode-2020]
Raspberry Pi setup:
1. Build angular front end `ng build`
1. Copy files to Raspbery Pi `scp -r BackEnd install.sh FrontEnd/dist pi@<pi ip>:~`
1. Login to Raspberry Pi `ssh pi@<pi ip>`
1. install dependencies `./install.sh`
1. cleanup `rm -rf BackEnd install.sh dist`
