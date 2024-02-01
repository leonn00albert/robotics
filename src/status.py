#!/usr/bin/env python3
# coding: utf8

import time
from rpi_ws281x import PixelStrip, Color

# Intialize the library (must be called once before other functions).
colormap = {
    'red': Color(255, 0, 0),
    'green': Color(0, 255, 0),
    'blue': Color(0, 0, 255),
    'white': Color(255, 255, 255),
    'black': Color(0, 0, 0),
    'yellow': Color(255, 255, 0),
    'magenta': Color(255, 0, 255),
    'cyan': Color(0, 255, 255),
    'orange': Color(255, 165, 0),
    'pink': Color(255, 192, 203),
    'purple': Color(128, 0, 128),
    'brown': Color(165, 42, 42),
    'gray': Color(128, 128, 128),
    'light_gray': Color(192, 192, 192),
    'dark_gray': Color(64, 64, 64)
}
# LED strip configuration:
LED_COUNT = 10        # Number of LED pixels.
LED_PIN = 18          # GPIO pin connected to the pixels (18 uses PWM!).
# LED_PIN = 10        # GPIO pin connected to the pixels (10 uses SPI /dev/spidev0.0).
LED_FREQ_HZ = 800000  # LED signal frequency in hertz (usually 800khz)
LED_DMA = 10          # DMA channel to use for generating signal (try 10)
LED_BRIGHTNESS = 20   # Set to 0 for darkest and 255 for brightest
LED_INVERT = False     # True to invert the signal (when using NPN transistor level shift)
LED_CHANNEL = 0       # set to '1' for GPIOs 13, 19, 41, 45 or 53
class Status():

    def __init__(self): 
        self.strip = PixelStrip(LED_COUNT, LED_PIN, LED_FREQ_HZ, LED_DMA, LED_INVERT, LED_BRIGHTNESS, LED_CHANNEL)
    def error(self,code=0):
        self.strip.begin()
        self.strip.show()
        time.sleep(1)
        self.strip.setPixelColor(code, Color(0, 0, 0))
        self.strip.setPixelColor(code, colormap['red'])
        self.strip.show()
        time.sleep(1)

    def ok(self,code=0):
        self.strip.begin()
        self.strip.show()
        time.sleep(1)
        self.strip.setPixelColor(code, Color(0, 0, 0))
        self.strip.setPixelColor(code, colormap['green'])
        self.strip.show()
        time.sleep(1)

    def info(self,code=0):
        self.strip.begin()
        self.strip.show()
        time.sleep(1)
        self.strip.setPixelColor(code, Color(0, 0, 0))
        self.strip.setPixelColor(code, colormap['blue'])
        self.strip.show()
        time.sleep(1)

    def warning(self,code=0):
        self.strip.begin()
        self.strip.show()
        time.sleep(1)
        self.strip.setPixelColor(code, Color(0, 0, 0))
        self.strip.setPixelColor(code, colormap['yellow'])
        self.strip.show()
        time.sleep(1)

status = Status()

status.error(1)
status.ok(2)
status.warning(2)
status.info(3)
