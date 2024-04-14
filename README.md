# Robotics Setup Guide
## Hardware

- **Raspberry Pi Model:** RPI 3a+
- **Motor Controller:** Waveshare 15364 [Motor Driver HAT](https://www.waveshare.com/wiki/Motor_Driver_HAT)

## Installation Steps

### Install Required Libraries

```bash
sudo apt-get install -y git python3-pip python3-smbus i2c-tools
```

    Install BCM2835 libraries


```bash
wget http://www.airspayce.com/mikem/bcm2835/bcm2835-1.70.tar.gz
tar zxvf bcm2835-1.70.tar.gz 
cd bcm2835-1.70/
sudo ./configure
sudo make && sudo make check && sudo make install
#For more information, please refer to the official website http://www.airspayce.com/mikem/bcm2835/
```
    Install wiringPi libraries
```bash
sudo apt-get install wiringpi
#For raspberry PI systems after May 2019 (those earlier may not need to be implemented), an upgrade may be required:
wget https://project-downloads.drogon.net/wiringpi-latest.deb
sudo dpkg -i wiringpi-latest.deb
gpio -v
#If gPIO -v is not installed, the 2.52 version will appear

```

    Install Python libraries

```bash
#python3
sudo apt-get update
sudo apt-get install python3-pip
sudo pip3 install RPi.GPIO
sudo apt-get install python3-serial

install the library on the Raspberry Pi with:

```



```bash
pip install git+https://github.com/orionrobots/Raspi_MotorHAT

```
Install LED drivers
```bash
sudo pip install rpi_ws281x
```
enable I2C and SPI in raspi-config


test i2x connection 

```bash
sudo i2cdetect -y 1
```

## Tests
Motor test
```
./test.sh motor
```

![](https://i.postimg.cc/cHY9B0RW/IMG-20240320-212820-127.jpg)
