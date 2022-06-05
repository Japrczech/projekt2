"""
projekt2.py: Hra Bull and Cows - druhý projekt do Engeto Online Python Akademie

author: Jaroslav Prudík
email: prudik.j@seznam.cz
discord: Jarek#3498
"""
# import balíčků (random = náhodný výběr)
import random

# základní definice a texty
cow = 0
bull = 0
oddelovac = "-" * 48

# seznam 4 náhodných číslic

nahodne_cislo = list()

while len(nahodne_cislo) < 4:
    cislo = random.randint(0,9)
    if cislo not in nahodne_cislo:
        nahodne_cislo.append(cislo)

#odstranění 0 na začátku, obrácením pořadí seznamu

if nahodne_cislo[0] == 0:
    nahodne_cislo.reverse()

# převedení seznamu na str

prvni_cislice = nahodne_cislo[0]
druha_cislice = nahodne_cislo[1]
treti_cislice = nahodne_cislo[2]
ctvrta_cislice = nahodne_cislo[3]
nahodne_cislo_seznam = list(f"{prvni_cislice}{druha_cislice}{treti_cislice}{ctvrta_cislice}")

#jen pro kontrolu
print(nahodne_cislo)

# úvodní text

print("Hi there!")
print(oddelovac)
print("I've generated a random 4 digit number for you.\nLet's play a bulls and cows game")
print(oddelovac)

# začátek hry - zadání čísla, rozdělení na jednotlivé číslice do seznamu

def seznam_zadane_cislo():
    zadane_cislo = input("Enter a number:")
    if len(zadane_cislo) == 4:
        print(oddelovac)
    else:
        print("the number doesnt have four numbers")
        quit()
    global zadane_cislo_seznam
    zadane_cislo_seznam = list(f"{zadane_cislo[0]}{zadane_cislo[1]}{zadane_cislo[2]}{zadane_cislo[3]}")

# počítání cow, vč. ukončení pokud cow = 4

def pocitani_cow(cow = 0):
    if zadane_cislo_seznam[0] == nahodne_cislo_seznam[0]:
        cow = cow + 1
    if zadane_cislo_seznam[1] == nahodne_cislo_seznam[1]:
        cow = cow + 1
    if zadane_cislo_seznam[2] == nahodne_cislo_seznam[2]:
        cow = cow + 1
    if zadane_cislo_seznam[3] == nahodne_cislo_seznam[3]:
        cow = cow + 1
    if cow <= 1:
        print("cow: ", cow)
    else:
        print("cows: ", cow)
    if cow == 4:
        print("Nahodné číslo bylo: ", nahodne_cislo, "vyhráls")
        quit()

# počítání bull
def pocitani_bull(bull = 0):
    if zadane_cislo_seznam[0] == nahodne_cislo_seznam[1]:
        bull = bull + 1
    elif zadane_cislo_seznam[0] == nahodne_cislo_seznam[2]:
        bull = bull + 1
    elif zadane_cislo_seznam[0] == nahodne_cislo_seznam[3]:
        bull = bull + 1
    if zadane_cislo_seznam[1] == nahodne_cislo_seznam[0]:
        bull = bull + 1
    elif zadane_cislo_seznam[1] == nahodne_cislo_seznam[2]:
        bull = bull + 1
    elif zadane_cislo_seznam[1] == nahodne_cislo_seznam[3]:
        bull = bull + 1
    if zadane_cislo_seznam[2] == nahodne_cislo_seznam[0]:
        bull = bull + 1
    elif zadane_cislo_seznam[2] == nahodne_cislo_seznam[1]:
        bull = bull + 1
    elif zadane_cislo_seznam[2] == nahodne_cislo_seznam[3]:
        bull = bull + 1
    if zadane_cislo_seznam[3] == nahodne_cislo_seznam[0]:
        bull = bull + 1
    elif zadane_cislo_seznam[3] == nahodne_cislo_seznam[1]:
        bull = bull + 1
    elif zadane_cislo_seznam[3] == nahodne_cislo_seznam[2]:
        bull = bull + 1
    if bull <= 1:
        print("bull: ", bull)
    else:
        print("bulls: ", bull)
    print(oddelovac)

# opakování hry

while cow < 4:
    seznam_zadane_cislo()
    pocitani_cow()
    pocitani_bull()



