import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings")

import django
django.setup()
import math

def conversor(valor, unidade1, unidade2):
    if(unidade1 == "dBm" and unidade2 == "dBm"):
        return valor + "dBm = " + valor + "dBm"
    if(unidade1 == "dBm" and unidade2 == "W"):
        return valor + "dBm = " + convertedBmW(valor) + "W"
    if(unidade1 == "dBm" and unidade2 == "dBW"):
        return valor + "dBm = " + convertedBmdBW(valor) + "dBW"
    if(unidade1 == "dBm" and unidade2 == "mW"):
        return valor + "dBm = " + convertedBmmW(valor) + "mW"

    if(unidade1 == "W" and unidade2 == "dBm"):
        return valor + "W = " + converteWdBm(valor) + "dBm"
    if(unidade1 == "W" and unidade2 == "W"):
        return valor + "W = " + valor + "W"
    if(unidade1 == "W" and unidade2 == "dBW"):
        return valor + "W = " + converteWdBW(valor) + "dBW"
    if(unidade1 == "W" and unidade2 == "mW"):
        return valor + "W = " + converteWmW(valor) + "mW"

    if(unidade1 == "dBW" and unidade2 == "dBm"):
        return valor + "dBW = " + convertedBWdBm(valor) + "dBm"
    if(unidade1 == "dBW" and unidade2 == "W"):
        return valor + "dBW = " + convertedBWW(valor) + "W"
    if(unidade1 == "dBW" and unidade2 == "dBW"):
        return valor + "dBW = " + valor + "dBW"
    if(unidade1 == "dBW" and unidade2 == "mW"):
        return valor + "dBW = " + convertedBWmW(valor) + "mW"

    if(unidade1 == "mW" and unidade2 == "dBm"):
        return valor + "mW = " + convertemWdBm(valor) + "dBm"
    if(unidade1 == "mW" and unidade2 == "W"):
        return valor + "dBW = " + convertemWW(valor) + "W"
    if(unidade1 == "mW" and unidade2 == "dBW"):
        return valor + "mW = " + convertemWdBW(valor) + "dBW"
    if(unidade1 == "mW" and unidade2 == "mW"):
        return valor + "mW = " + valor + "mW"



def convertedBmdBW(original):
    valorOriginal = float(original)
    valorConvertido = 0

    valorConvertido = valorOriginal-30
    string = str(valorConvertido)
    return string

def convertedBmW(original):
    valorOriginal = float(original)
    valorConvertido = 0

    valorConvertido = 10**((valorOriginal-30)/10)
    string = str(valorConvertido)
    return string

def convertedBmmW(original):
    valorOriginal = float(original)
    valorConvertido = 0

    valorConvertido = 10**(valorOriginal/10)
    string = str(valorConvertido)
    return string

def comvertedBmdBw(original):
    valorOriginal = float(original)
    valorConvertido = 0
    
    valorConvertido = valorOriginal + 30   
    string = str(valorConvertido)
    return string

def converteWdBm(original):
    valorOriginal = float(original)
    valorConvertido = 0

    valorConvertido = (10*math.log10(valorOriginal / 1)) + 30
    string = str(valorConvertido)
    return string

def converteWmW(original):
    valorOriginal = float(original)
    valorConvertido = 0

    valorConvertido = valorOriginal * 1000
    string = str(valorConvertido)
    return string

def converteWdBW(original):
    valorOriginal = float(original)
    valorConvertido = 0

    valorConvertido = (10*math.log10(valorOriginal / 1))
    string = str(valorConvertido)
    return string

def convertedBWW(original):
    valorOriginal = float(original)
    valorConvertido = 0

    valorConvertido = 10**(valorOriginal/10)
    string = str(valorConvertido)
    return string


def convertedBWdBm(original):
    valorOriginal = float(original)
    valorConvertido = 0

    valorConvertido = valorOriginal+30
    string = str(valorConvertido)
    return string

def convertedBWmW(original):
    valorOriginal = float(original)
    valorConvertido = 0

    valorConvertido = (10**(valorOriginal/10)) * 1000
    string = str(valorConvertido)
    return string

def convertemWdBm(original):
    valorOriginal = float(original)
    valorConvertido = 0

    valorConvertido = (10*math.log10(valorOriginal / 1))
    string = str(valorConvertido)
    return string

def convertemWW(original):
    valorOriginal = float(original)
    valorConvertido = 0

    valorConvertido = valorOriginal / 1000
    string = str(valorConvertido)
    return string

def convertemWdBW(original):
    valorOriginal = float(original)
    valorConvertido = 0

    valorConvertido = (10*math.log10((valorOriginal/1000) / 1))
    string = str(valorConvertido)
    return string

def calculateNyquist(b, v):
    b = b * (10**6)  # convertendo MHz para Hz
    resultado = b * v * math.log2(v)
    string = str(resultado)
    return "Debito:" + string

def calculateShannon(snr, b):
    b = b * (10**6)  # convertendo MHz para Hz
    snr = 10 ** (snr / 10)  # convertendo SNR de dB para escala linear
    resultado = b * math.log2(1 + snr)
    string = str(resultado)
    return string