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

# převedení seznamu na str
prvni_cislice = nahodne_cislo[0]
druha_cislice = nahodne_cislo[1]
treti_cislice = nahodne_cislo[2]
ctvrta_cislice = nahodne_cislo[3]
nahodne_cislo_seznam = list(f"{prvni_cislice}{druha_cislice}{treti_cislice}{ctvrta_cislice}")

# jen pro kontrolu
# print(nahodne_cislo)

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
        print("the number doesnt have four numbers or not numeric")
    # seznam ze zadaného čísla
    global zadane_cislo_seznam
    zadane_cislo_seznam = list(f"{zadane_cislo[0]}{zadane_cislo[1]}{zadane_cislo[2]}{zadane_cislo[3]}")
    # kontrola unikátnosti číslic
    if len(zadane_cislo_seznam) != len(set(zadane_cislo_seznam)):
        print("The numbers mustn\'t be same")
    # kontrola - nesmí být 0 na začátku
    if zadane_cislo[0] == "0":
        print("0 mustn\'t be in the first place")


# počítání bull ikdyž se jmenuje cow:-)
def pocitani_cow(cow=0):
    if zadane_cislo_seznam[0] == nahodne_cislo_seznam[0]:
        cow = cow + 1
    if zadane_cislo_seznam[1] == nahodne_cislo_seznam[1]:
        cow = cow + 1
    if zadane_cislo_seznam[2] == nahodne_cislo_seznam[2]:
        cow = cow + 1
    if zadane_cislo_seznam[3] == nahodne_cislo_seznam[3]:
        cow = cow + 1
    # rozlišení jednotného a množného čísla
    if cow <= 1:
        print("bull: ", cow)
    else:
        print("bulls: ", cow)
    if cow == 4:
        print(f"Correct, you've guessed the right number in {pocet_zadani}  guesses!")
        quit()


# počítání cow ikdyž se jmenuje bull :-)
def pocitani_bull(bull=0):
    if zadane_cislo_seznam[0] == nahodne_cislo_seznam[1]:
        bull = bull + 1
    if zadane_cislo_seznam[0] == nahodne_cislo_seznam[2]:
        bull = bull + 1
    if zadane_cislo_seznam[0] == nahodne_cislo_seznam[3]:
        bull = bull + 1
    if zadane_cislo_seznam[1] == nahodne_cislo_seznam[0]:
        bull = bull + 1
    if zadane_cislo_seznam[1] == nahodne_cislo_seznam[2]:
        bull = bull + 1
    if zadane_cislo_seznam[1] == nahodne_cislo_seznam[3]:
        bull = bull + 1
    if zadane_cislo_seznam[2] == nahodne_cislo_seznam[0]:
        bull = bull + 1
    if zadane_cislo_seznam[2] == nahodne_cislo_seznam[1]:
        bull = bull + 1
    if zadane_cislo_seznam[2] == nahodne_cislo_seznam[3]:
        bull = bull + 1
    if zadane_cislo_seznam[3] == nahodne_cislo_seznam[0]:
        bull = bull + 1
    if zadane_cislo_seznam[3] == nahodne_cislo_seznam[1]:
        bull = bull + 1
    if zadane_cislo_seznam[3] == nahodne_cislo_seznam[2]:
        bull = bull + 1
    # rozlišení jednotného a množného čísla
    if bull <= 1:
        print("cow: ", bull)
    else:
        print("cows: ", bull)
    # čára
    print(oddelovac)


# zajištění opakování hry
while cow < 4:
    seznam_zadane_cislo()
    pocitani_cow()
    pocitani_bull()
