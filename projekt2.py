"""
projekt2.py: Hra Bull and Cows - druhý projekt do Engeto Online Python Akademie

author: Jaroslav Prudík
email: prudik.j@seznam.cz
discord: Jarek#3498
"""
# import balíčků (random = náhodný výběr)
import random

# základní proměnné
cow = 0
bull = 0
oddelovac = "-" * 48
pocet_zadani = 0

# seznam 4 náhodných nestejných číslic
nahodne_cislo = list()
while len(nahodne_cislo) < 4:
    cislo = random.randint(0, 9)
    if cislo not in nahodne_cislo:
        nahodne_cislo.append(cislo)

# odstranění 0 na začátku, obrácením pořadí seznamu
if nahodne_cislo[0] == 0:
    nahodne_cislo.reverse()

# převedení na string. nahodne_cislo nelze převést na string, protože pak nejde zajistit neopakování číslic
nahodne_cislo_seznam = list()
for cislo in nahodne_cislo:
    nahodne_cislo_seznam.append(str(cislo))

# jen pro kontrolu
#print(nahodne_cislo_seznam)

# úvodní text
print("Hi there!")
print(oddelovac)
print("I've generated a random 4 digit number for you.\nLet's play a bulls and cows game")
print(oddelovac)


# začátek hry - zadání čísla, rozdělení na jednotlivé číslice do seznamu, kontroly dle zadání.
def seznam_zadane_cislo():
    zadane_cislo = input("Enter a number:")
    print(oddelovac)
    # počítadlo zadání čísla
    global pocet_zadani
    if zadane_cislo != 0:
        pocet_zadani = pocet_zadani + 1
        print(f"guess: {pocet_zadani}")
    # kontrola číslo je číslo a čtyřmístné
    if zadane_cislo.isnumeric() and len(zadane_cislo) == 4:
        pass
    elif len(zadane_cislo) < 4:
        print("The number has a little numbers! Stop")
        quit()
    else:
        print("the number doesn\'t have four numbers or not numeric")
    # seznam ze zadaného čísla
    global zadane_cislo_seznam
    zadane_cislo_seznam = list(f"{zadane_cislo[0]}{zadane_cislo[1]}{zadane_cislo[2]}{zadane_cislo[3]}")
    # kontrola unikátnosti číslic
    if len(zadane_cislo_seznam) != len(set(zadane_cislo_seznam)):
        print("The numbers mustn\'t be same")
    # kontrola - nesmí být 0 na začátku
    if zadane_cislo[0] == "0":
        print("0 mustn\'t be in the first place")


# počítání bull
def pocitani_bull(bull=0):
    if zadane_cislo_seznam[0] == nahodne_cislo_seznam[0]:
        bull = bull + 1
    if zadane_cislo_seznam[1] == nahodne_cislo_seznam[1]:
        bull = bull + 1
    if zadane_cislo_seznam[2] == nahodne_cislo_seznam[2]:
        bull = bull + 1
    if zadane_cislo_seznam[3] == nahodne_cislo_seznam[3]:
        bull = bull + 1
    # rozlišení jednotného a množného čísla
    if bull <= 1:
        print("bull: ", bull)
    else:
        print("bulls: ", bull)
    if bull == 4:
        print(f"Correct, you've guessed the right number in {pocet_zadani} guesses!")
        print(oddelovac)
        quit()


# počítání cow
def pocitani_cow(cow=0):
    if zadane_cislo_seznam[0] == nahodne_cislo_seznam[1]:
        cow = cow + 1
    if zadane_cislo_seznam[0] == nahodne_cislo_seznam[2]:
        cow = cow + 1
    if zadane_cislo_seznam[0] == nahodne_cislo_seznam[3]:
        cow = cow + 1
    if zadane_cislo_seznam[1] == nahodne_cislo_seznam[0]:
        cow = cow + 1
    if zadane_cislo_seznam[1] == nahodne_cislo_seznam[2]:
        cow = cow + 1
    if zadane_cislo_seznam[1] == nahodne_cislo_seznam[3]:
        cow = cow + 1
    if zadane_cislo_seznam[2] == nahodne_cislo_seznam[0]:
        cow = cow + 1
    if zadane_cislo_seznam[2] == nahodne_cislo_seznam[1]:
        cow = cow + 1
    if zadane_cislo_seznam[2] == nahodne_cislo_seznam[3]:
        cow = cow + 1
    if zadane_cislo_seznam[3] == nahodne_cislo_seznam[0]:
        cow = cow + 1
    if zadane_cislo_seznam[3] == nahodne_cislo_seznam[1]:
        cow = cow + 1
    if zadane_cislo_seznam[3] == nahodne_cislo_seznam[2]:
        cow = cow + 1
    # rozlišení jednotného a množného čísla
    if cow <= 1:
        print("cow: ", cow)
    else:
        print("cows: ", cow)
    # čára
    print(oddelovac)

# zajištění opakování hry
while bull < 4:
    seznam_zadane_cislo()
    pocitani_bull()
    pocitani_cow()
