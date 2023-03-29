import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings")

import django
django.setup()
import math

def converteWdbW(original):
    valorOriginal = float(original)
    valorConvertido = 0

    valorConvertido = 10*math.log10(valorOriginal / 1.10)
    string = str(round(valorConvertido))
    print(string + "dbW")
        

def comvertedBmdBw(original):
    valorOriginal = float(original)
    valorConvertido = 0
    
    valorConvertido = valorOriginal + 30   
    
    string = str(valorConvertido)
    print(string + " dBw")


def convertedBWW(original):
    valorOriginal = float(original)
    valorConvertido = 0

    valorConvertido = 10**(valorOriginal/10)
    string = str(valorConvertido)
    print(string + "W")

