# Example of internal RGB light for Desert Media Art
# Sri Pranav Srivatsavai
# 2022-09-07

# Uses code from Adafruit
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

#i = 0
# inital opening of the eyes
brightness = 0
while brightness <= 0.35:
    led.brightness = brightness
    brightness = (brightness+0.0001)
    led[0] = (255,255,255)

# scene - pleasant
i = 0
while i < 8000:
    led.brightness = brightness
    brightness = (brightness+0.001) % 1
    led[0] = (255,255,0)
    i+=1

#scene - panzar enters
j = 0
while j < 0.25:
    led.brightness = 1
    led[0] = (255,0,0)
    time.sleep(1)
    led.brightness = 0.5
    time.sleep(1)
    led.brightness = 1
    time.sleep(1)
    j+=0.1

# scene - shooting begins
k = 0;
while k < 1.3:
    led.brightness = 0.5
    led[0] = (255,0,0)
    time.sleep(0.25)
    led[0] = (0,0,255)
    time.sleep(0.25)

    led.brightness = 1
    led[0] = (255,0,0)
    time.sleep(0.25)
    led[0] = (0,0,255)
    time.sleep(0.25)

    k+=0.1

# scene - stops shooting - rainbow setting
i = 0
a = 0
while a<1000:
    i = (i + 1) % 256  # run from 0 to 255
    led.fill(colorwheel(i))
    time.sleep(0.01)
    a+=1


# scene - yellow lights "put him in the background"
w = 0
while w < 3750:
    led.brightness = brightness
    brightness = (brightness+0.001) % 1
    led[0] = (255,255,0)
    w+=1

# scene - focus on yoghurt
i = 0
a = 0
while a<500:
    i = (i + 1) % 256  # run from 0 to 255
    led.fill(colorwheel(i))
    time.sleep(0.01)
    a+=1
