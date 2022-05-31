import RPi.GPIO as GPIO
import time

servoPIN = 17
armPin = 22


def servoFlip():
  GPIO.setmode(GPIO.BCM)
  GPIO.setup(servoPIN, GPIO.OUT)

  p = GPIO.PWM(servoPIN, 50) # GPIO 17 for PWM with 50Hz
  print('-> Servo Flip')
  p.start(5) # Initialization
  time.sleep(0.5)
  p.ChangeDutyCycle(2.5)
  time.sleep(0.5)
  p.ChangeDutyCycle(5)
  time.sleep(0.5)
  p.stop()
  
  GPIO.cleanup()

def armUp():
  GPIO.setmode(GPIO.BCM)
  GPIO.setup(armPin, GPIO.OUT)

  p = GPIO.PWM(armPin, 50) # GPIO 27 for PWM with 50Hz
  print('-> Arm Up')
  p.start(5) # Initialization
  time.sleep(1.5)
  p.stop()
  
  GPIO.cleanup()

def armDown():
  GPIO.setmode(GPIO.BCM)
  GPIO.setup(armPin, GPIO.OUT)

  p = GPIO.PWM(armPin, 50) # GPIO 27 for PWM with 50Hz
  print('-> Arm Up')
  p.start(5) # Initialization
  time.sleep(1.5)

  count = 5

  while count >= 3.625:
    count -= 0.01
    p.ChangeDutyCycle(count)
    time.sleep(0.0025)
  time.sleep(0.5)
  # time.sleep(1)
  # p.ChangeDutyCycle(5)
  # time.sleep(0.5)
  p.stop()
  
  GPIO.cleanup()

def armToCam():
  GPIO.setmode(GPIO.BCM)
  GPIO.setup(armPin, GPIO.OUT)

  p = GPIO.PWM(armPin, 50) # GPIO 27 for PWM with 50Hz
  print('-> Arm to cam')
  p.start(5) # Initialization
  time.sleep(1.5)

  count = 5

  while count >= 4.5:
    count -= 0.01
    p.ChangeDutyCycle(count)
    time.sleep(0.0025)
  time.sleep(0.5)
  # time.sleep(1)
  # p.ChangeDutyCycle(5)
  # time.sleep(0.5)
  p.stop()
  
  GPIO.cleanup()

# def armDown():



# try:
#   while True:
#     print("5")
#     p.ChangeDutyCycle(5)
#     time.sleep(1)
#     print("2.5")
#     p.ChangeDutyCycle(2.5)
#     time.sleep(0.5)
# except KeyboardInterrupt:
#   p.stop()
#   GPIO.cleanup()

  