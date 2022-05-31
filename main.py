from functions import  floor, right, back, left, under, down, floor_prime, right_prime, back_prime, left_prime, under_prime, down_prime, init
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BOARD)

string=["F", "R", "B", "L", "U", "D", "F'", "R'", "B'", "L'", "U'", "D'"]

buttonPin = #pin à définir

GPIO.setup(buttonPin, GPIO.IN, pull_up_down=GPIO.PUD_UP)

def string_to_moves(string):
    for letter in string:
        #fonction
        if letter == "F":
            floor()

        if letter == "R":
            right()

        if letter == "B":
            back()

        if letter == "L":
            left()

        if letter == "U":
            under()

        if letter == "D":
            down()

        if letter == "F'":
            floor_prime()

        if letter == "R'":
            right_prime()

        if letter == "B'":  
            back_prime()

        if letter == "L'":
            right_prime()

        if letter == "U'":
            under_prime()

        if letter == "D'":
            down_prime()
        

while True:
  buttonState = GPIO.input(buttonPin)
  if buttonState == False:
    # Initialisation
    init()
    #appelle la fonction de mouvement des moteurs
    string_to_moves(string)
  else:
    #NE RIEN FAIRE


