from time import sleep 
import RPi.GPIO as gpio 

DIR = 20 
STEP = 21 
CW =1 
CCW =0 

# gpio.setmode(gpio.BCM) 
# gpio.setup(DIR, gpio.OUT) 
# gpio.setup(STEP, gpio.OUT) 
# gpio.output(DIR,CW)

def nemaTest():
    # Main body of code
    print("-> Nema Init")
    gpio.cleanup() 
    gpio.setmode(gpio.BCM) 
    gpio.setup(DIR, gpio.OUT) 
    gpio.setup(STEP, gpio.OUT) 

    gpio.output(DIR,CW) 

    for x in range(200): 

        gpio.output(STEP,gpio.HIGH) 
        sleep(.0005) 
        gpio.output(STEP,gpio.LOW) 
        sleep(.0005) 

    sleep(1) 
    gpio.output(DIR,CCW) 

    for x in range(200): 

        gpio.output(STEP,gpio.HIGH) 
        sleep(.0005) 
        gpio.output(STEP,gpio.LOW) 
        sleep(.0005)

    sleep(1)
    gpio.cleanup() 

def nemaCW():
    gpio.cleanup() 
    print("-> Clockwise Rotation")
    gpio.setmode(gpio.BCM) 
    gpio.setup(DIR, gpio.OUT) 
    gpio.setup(STEP, gpio.OUT) 
    gpio.output(DIR,CW)

    for x in range(200): 

        gpio.output(STEP,gpio.HIGH) 
        sleep(.0005) 
        gpio.output(STEP,gpio.LOW) 
        sleep(.0005)

    gpio.cleanup() 

def nemaCCW():
    gpio.cleanup() 
    print("-> Counter Clockwise Rotation")
    gpio.setmode(gpio.BCM) 
    gpio.setup(DIR, gpio.OUT) 
    gpio.setup(STEP, gpio.OUT) 
    gpio.output(DIR,CCW)


    for x in range(200): 
        gpio.output(STEP,gpio.HIGH) 
        sleep(.0005) 
        gpio.output(STEP,gpio.LOW) 
        sleep(.0005)

    gpio.cleanup() 


# try:       
# except KeyboardInterrupt: # If there is a KeyboardInterrupt (when you press ctrl+c), exit the program and cleanup 
#     print("Cleaning up!") 
#     gpio.cleanup()  