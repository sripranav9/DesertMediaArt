# Exercise 1 – Internal RGB light
# Sri Pranav Srivatsavai
# Desert Media Art
# 2022-09-11
# Description: This code is an attempt at setting the mood using lighting for a short scene from Mr. Bean's movie.
# The light is set for 0:00 - 1:48 mins of the video
# Link to the video: https://www.youtube.com/watch?v=a-VLZ0T8WMo

# Uses code from Adafruit:
# https://learn.adafruit.com/adafruit-feather-m4-express-atsamd51/circuitpython-internal-rgb-led

    # SPDX-FileCopyrightText: 2018 Kattni Rembor for Adafruit Industries
    #
    # SPDX-License-Identifier: MIT

    # SPDX-FileCopyrightText: 2018 Kattni Rembor for Adafruit Industries
    #
    # SPDX-License-Identifier: MIT

    # SPDX-FileCopyrightText: 2018 Kattni Rembor for Adafruit Industries
    #
    # SPDX-License-Identifier: MIT

"""CircuitPython Essentials Internal RGB LED rainbow example"""
import time
import board
from rainbowio import colorwheel

if hasattr(board, "APA102_SCK"):
    import adafruit_dotstar

    led = adafruit_dotstar.DotStar(board.APA102_SCK, board.APA102_MOSI, 1)
else:
    import neopixel

    led = neopixel.NeoPixel(board.NEOPIXEL, 10)

#set the brightness of the bulb to 0 initially
brightness = 0

# scene - inital: Bean opens his eyes
# NOTE: the numbers for the while loop are chosen after testing with the time of each scene in the video
# increase brightness gradually and proceed to next scene once the time for that scene is over
while brightness <= 0.35:
    led.brightness = brightness
    brightness = (brightness+0.0001) # increment brightness
    led[0] = (255,255,255) # (r,g,b) format

# scene - pleasant: Bean looks around
i = 0
# yellow light turns on and gradually goes off repeatedly
while i < 8000:
    led.brightness = brightness
    brightness = (brightness+0.001) % 1
    led[0] = (255,255,0) # (r,g,b) format
    i+=1 # increment i by 1

#scene - fear: panzer enters
j = 0 # used in the while loop to end the loop at a specific point
# Red light goes on and off at 2 different brightness settings
while j < 0.25:
    led.brightness = 1
    led[0] = (255,0,0) # red color
    time.sleep(1) # wait for a second
    led.brightness = 0.5
    time.sleep(1)
    led.brightness = 1
    time.sleep(1)
    j+=0.1 # increment j by 0.1

# scene - chaos: shooting begins
k = 0; # used in the while loop to end the loop after a specific point
while k < 1.3:
    led.brightness = 0.5 # 50% brightness
    led[0] = (255,0,0) # red light
    time.sleep(0.25)
    led[0] = (0,0,255) # blue light
    time.sleep(0.25)
    
    led.brightness = 1 # 100% brightness
    led[0] = (255,0,0 # red light
    time.sleep(0.25)
    led[0] = (0,0,255) # blue light
    time.sleep(0.25)
    
    k+=0.1 # increment k by 0.1

# Inspiration: Adafruit code
# scene - confusion: shooting stops
i = 0 # for controlling brightness in the loop
a = 0 # to end the loop at a specific point
while a<1000:
    i = (i + 1) % 256  # run from 0 to 255
    led.fill(colorwheel(i))
    time.sleep(0.01)
    a+=1
    
# scene - normal: director says "put him in the background"
w = 0 # to end the loop later
while w < 3750:
    led.brightness = brightness
    brightness = (brightness+0.001) % 1
    led[0] = (255,255,0) # yellow light
    w+=1 # increment w by 1
    
# scene - focus: focus on yoghurt
i = 0 # controlling the brightness in the loop
a = 0 # to end the loop later at a specific point
while a<500:
    i = (i + 1) % 256  # run from 0 to 255 and again
    led.fill(colorwheel(i)) # rainbow pattern
    time.sleep(0.01)
    a+=1 # increment a by 1
