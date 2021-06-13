Materials:
1 x HDMI Cable ($6) [https://www.adafruit.com/product/2775]
1 x Raspberry Pi 3 A+ ($25) [https://www.adafruit.com/product/4027]
1 x 5v 2.5a supply ($8) [https://www.adafruit.com/product/1995]
1 x 8GB SD Card
8 x Photo Transistor ($4) [https://www.adafruit.com/product/2831]
8 x 5.6kohm Resistor ($1)
8 x 1kohm Resistor ($1)

F to M jumper wires ($2) [https://www.adafruit.com/product/1954]
1 x Breadboard ($5) [https://www.adafruit.com/product/64]

1 x HDMI Display ($42) [https://www.amazon.com/Yasoca-Inch-Monitor-HDMI-Raspberry/dp/B089YSHMYS/ref=sr_1_19?dchild=1&keywords=hdmi%2Bdisplay%2B7%2Binch&qid=1612496742&refinements=p_85%3A2470955011&rnid=2470954011&rps=1&sr=8-19&th=1]
Total: $93

Raspberry Pi setup:
1. Using Belena Etcher, burn Raspbian Lite OS image to the SD Card
1. Connect keyboard and monitor to Raspberry Pi, and let it startup
1. Login using username 'pi' and password 'raspberry'
1. Run 'sudo raspi-config' to enable WiFi and login to your network
  1. Select System Options->Wireless LAN and enter your SSID and password
  1. Select Interface Options->SSH to enable SSH access to your Raspberry Pi
1. Restart the Raspberry Pi to let it connect to your network
1. Run 
1. After it reboots, login again, and type the 'ifconfig' command to get the IP address for your network

From your computer:
1. Copy files to Raspbery Pi `scp -r backend frontend web_frontend/dist install.sh pi@<pi ip>:~`
1. Login to Raspberry Pi `ssh pi@<pi ip>`
1. install dependencies `./install.sh`
1. cleanup `rm -rf BackEnd install.sh dist`
