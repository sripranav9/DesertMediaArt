print("Hello Desert Media Art!")
print("Let's Blink")

# Importing necessary libraries
import board 
import digitalio
import time

print ("It is now " + str(time.monotonic()))
# print ('The basic LED is attached to pin' + str(board.LED))

# This variable gives us access to the hardware pin
led = digitalio.DigitalInOut(board.LED) # the way we access the pin

# set the pin as the output so that we can turn it on/off
led.direction = digitalio.Direction.OUTPUT 

startTime = time.monotonic()
secondsToBlink = 5

print("Starting to Blink")

while (time.monotonic() - startTime) < secondsToBlink:
    led.value = True # ON the LED
    time.sleep(0.5/2) # delay
    led.value = False # OFF the LED
    time.sleep(0.5/2) # delay
    
    # sepcial notation of python to say take this and fill in what is inside the bracket
    print("  time - %.2f" % time.monotonic()) # space to debug easily
    
    if led.value == True:
        print("   1")
    else:
        print("   0")
    
print("All Done")
