"""
projekt2.py: Hra Bull and Cows - druhý projekt do Engeto Online Python Akademie

author: Jaroslav Prudík
email: prudik.j@seznam.cz
discord: Jarek#3498
"""
# import balíčků (random = náhodný výběr)
import random
cow = 0
bull = 0
# základní definice a texty

oddelovac = "-" * 48
#cow = 0
#bull = 0
# vygenerované náhodné číslo jako seznam jednotlivých číslic
#nahodne_cislo = list(f"{int(prvni_cislice)}{int(druha_cislice)}{int(treti_cislice)}{int(ctvrta_cislice)}")

nahodne_cislo = list()

while len(nahodne_cislo) < 4:
    cislo = random.randint(1,9)
    if cislo not in nahodne_cislo:
        nahodne_cislo.append(cislo)

prvni_cislice = nahodne_cislo[0]
druha_cislice = nahodne_cislo[1]
treti_cislice = nahodne_cislo[2]
ctvrta_cislice = nahodne_cislo[3]
nahodne_cislo = list(f"{prvni_cislice}{druha_cislice}{treti_cislice}{ctvrta_cislice}")

print(nahodne_cislo)

# úvodní text
print("Hi there!")
print(oddelovac)
print("I've generated a random 4 digit number for you.\nLet's play a bulls and cows game")
print(oddelovac)

# začátek hry - zadání čísla, rozdělení na jednotlivé číslice do seznamu


#cow = 0
#bull = 0

#def zadani_cisla(zadane_cislo1_seznam):
#zadane_cislo1_seznam = list(f"{zadane_cislo1[0]}{zadane_cislo1[1]}{zadane_cislo1[2]}{zadane_cislo1[3]}")


def seznam_zadane_cislo():
    zadane_cislo1 = input("Enter a number:")
    if len(zadane_cislo1) == 4:
        print(oddelovac)
    else:
        print("the number doesnt have four numbers")
        quit
    global zadane_cislo1_seznam
    zadane_cislo1_seznam = list(f"{zadane_cislo1[0]}{zadane_cislo1[1]}{zadane_cislo1[2]}{zadane_cislo1[3]}")


# zajištění čtyřmístného čísla



def pocitani_cow(cow = 0):
    if zadane_cislo1_seznam[0] == nahodne_cislo[0]:
        cow = cow + 1
    if zadane_cislo1_seznam[1] == nahodne_cislo[1]:
        cow = cow + 1
    if zadane_cislo1_seznam[2] == nahodne_cislo[2]:
        cow = cow + 1
    if zadane_cislo1_seznam[3] == nahodne_cislo[3]:
        cow = cow + 1
    print("cow: ", cow)
    if cow == 4:
        print("Nahodné číslo bylo: ", nahodne_cislo, "vyhráls")
        quit()
# print(zadane_cislo1_seznam)

def pocitani_bull(bull = 0):
    if zadane_cislo1_seznam[0] == nahodne_cislo[1]:
        bull = bull + 1
    elif zadane_cislo1_seznam[0] == nahodne_cislo[2]:
        bull = bull + 1
    elif zadane_cislo1_seznam[0] == nahodne_cislo[3]:
        bull = bull + 1
    if zadane_cislo1_seznam[1] == nahodne_cislo[0]:
        bull = bull + 1
    elif zadane_cislo1_seznam[1] == nahodne_cislo[2]:
        bull = bull + 1
    elif zadane_cislo1_seznam[1] == nahodne_cislo[3]:
        bull = bull + 1
    if zadane_cislo1_seznam[2] == nahodne_cislo[0]:
        bull = bull + 1
    elif zadane_cislo1_seznam[2] == nahodne_cislo[1]:
        bull = bull + 1
    elif zadane_cislo1_seznam[2] == nahodne_cislo[3]:
        bull = bull + 1
    if zadane_cislo1_seznam[3] == nahodne_cislo[0]:
        bull = bull + 1
    elif zadane_cislo1_seznam[3] == nahodne_cislo[1]:
        bull = bull + 1
    elif zadane_cislo1_seznam[3] == nahodne_cislo[2]:
        bull = bull + 1
    print("bull: ", bull)

while cow < 4:
    seznam_zadane_cislo()
    pocitani_cow()
    pocitani_bull()



