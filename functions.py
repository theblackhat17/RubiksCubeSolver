#-- coding: utf-8 --
# Path: main.py
# TH3_BL@CK_H@T


"""
⛔️ Le stepper n'est pas inclu dans ce code, je dois donc l'ajouter pour les fonctions "S" et "S'" qui utilise ce type de moteur. Pour rappel, à 90° et -90° 
"""

"""
⛔️ Voir si les " ' " ne perturbent pas la lecture de la chaîne de caractère
"""


"""
Pour configurer le projet à la raspberry, j'utilise les commandes de ce site : https://raspberry-pi.fr/servomoteur-raspberry-pi/
Les étapes à réaliser sont donc à l'intérieur
"""


import RPi.GPIO as GPIO
from trad_functions import *

servoPIN = 17
armPin = 22


"""
Je pose mes fonctions
"""

"""
Ici je pose mes lignes de code permettant de configurer les ports GPIO utilisé sur la raspberry par les servos
"""

"""  
Je pose mes conditions de fonctions par rapport à la string obtenue  
"""
def init():
    flipInit()
    initSolver()

def floor():
    flip()
    armDown()
    clockwise()
    armUp()
    flip()
    flip()
    flip()

def right ():
    clockwise()
    flip()
    armDown()
    clockwise()
    armUp()
    flip()
    flip()
    flip()
    anticlockwise()

def back():
    flip()
    flip()
    armDown()
    clockwise()
    armUp()
    flip()
    flip()

def left():
    flip()
    anticlockwise()
    flip()
    armDown()
    anticlockwise()
    armUp()
    anticlockwise()
    flip()
    anticlockwise()

def under():
    armDown()
    clockwise()
    armUp()

def down():
    flip()
    armDown()
    anticlockwise()
    armUp()
    flip()
    flip()
    flip()

#Sens contraire du cube

def floor_prime():
    flip()
    armDown()
    anticlockwise()
    armUp()
    flip()
    flip()
    flip()

def right_prime():
    clockwise()
    flip()
    armDown()
    anticlockwise()
    armUp()
    flip()
    flip()
    flip()
    anticlockwise()

def back_prime():
    flip()
    flip()
    armDown()
    anticlockwise()
    armUp()
    flip()
    flip()

def left_prime():
    flip()
    anticlockwise()
    flip()
    armDown()
    clockwise()
    armUp()
    anticlockwise()
    flip()
    anticlockwise()

def under_prime():
    armDown()
    anticlockwise()
    armUp()

def down_prime():
    flip()
    armDown()
    clockwise()
    armUp()
    flip()
    flip()
    flip()

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