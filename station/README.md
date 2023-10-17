# BOM Per Station
* $35 - Le Potato [https://www.amazon.com/dp/B0BDR2LWPC]
* $4  - 32gb microSD [https://www.amazon.com/dp/B07V1WC64X]
* $6  - USB Speaker [https://www.aliexpress.us/item/3256805016438808.html]
* $3  - USB Power Breakout [https://www.amazon.com/dp/B09W2QHL2P]
* $10 - RFID Card Reader [https://www.amazon.com/dp/B0B4BJK3W2]
* $3  - Ethernet Patch Cable [https://www.amazon.com/dp/B003EDZEDI]

Total Per Station: $61

# BOM Per Track
* $45 - 16 ports unmanaged switch 2x[https://www.amazon.com/dp/B07PFYM5MZ]
* $3  - Ethernet Patch Cable [https://www.amazon.com/dp/B003EDZEDI]
* $13 - USB Ethernet Adapter [https://www.amazon.com/dp/B00YUU3KC6]
* $10 - 30 Pack RFID Cards [https://www.amazon.com/gp/product/B07P8NCX55]

Total Per Track: $71
Total for 8 statsions: $498

# Le Potato Setup
1. Use Raspberry Pi Imager to burn Raspbian 11 lite to microSD cards [https://distro.libre.computer/ci/raspbian/11/2023-05-03-raspbian-bullseye-arm64%2Baml-s905x-cc.img.xz]
2. Enable SSH by creating empty file in boot partition called `ssh`
3. Set initial username and password by creating file called `userconf` containing username:encryptedpassword.  You can get the encrypted password via the command `openssl passwd -6`
4. Enable connection sharing to your Ethernet port on your development PC
5. Insert the microSD card into the Le Potato, connect an ethernet cable to your development PC, and power up the board.
6. Find the IP address of your Le Potato after it boots (this will take a little time, look for the green light to come on)
7. SSH into your Le Potato
8. Enable sound using `alsamixer`
  * Set volume (ACODEC) to 80
  * Set AIU ACODEC OUT EN to ON (Press M key)
  * Set AIU ACODEC SRC to I2S
9. Execute `sudo alsactl store` to persist settings

# Resources
[https://www.raspberrypi.com/documentation/computers/remote-access.html#setting-up-an-ssh-server]