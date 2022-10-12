# 12 October 2022, In-class Exercise

# SPDX-FileCopyrightText: 2018 Anne Barela for Adafruit Industries
# SPDX-License-Identifier: MIT
# Source: https://learn.adafruit.com/make-it-change-potentiometers/circuitpython

# Modified by Sri Pranav Srivatsavai
# Under the guidance of Professor mang
# Desert Media Art – Photocell and Potentiometer

import time
import board
from analogio import AnalogIn

photoCell = AnalogIn(board.A1)  # potentiometer connected to A1, power & ground

darkThreshold = 28000
brightThreshold = 45000

while True:

    brightness = photoCell.value
    print((brightness,))      # Display value
    
    if (brightness > brightThreshold):
        print('bright')
    if (brightness < darkThreshold):
        print('dark')

    time.sleep(0.25)                   # Wait a bit before checking the value again
