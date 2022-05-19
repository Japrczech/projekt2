"""
projekt2.py: Hra Bull and Cows - druhý projekt do Engeto Online Python Akademie

author: Jaroslav Prudík
email: prudik.j@seznam.cz
discord: Jarek#3498
"""
#import balíčků (random = náhodný výběr)
import random
#seznam pro výběr jednotlivých číslic. cislo1 pro první číslici bez 0
cisla = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
cislo1 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(random.choice(cisla))

#základní definice a texty

oddelovac = "-" * 48
#jednotlivé číslice čtyřmístného náhodného čísla
prvni_cislice = random.choice(cislo1)
druha_cislice = random.choice(cisla)
treti_cislice = random.choice(cisla)
ctvrta_cislice = random.choice(cisla)

#vygenerované náhodné číslo jako seznam jednotlivých číslic
nahodne_cislo = list(f"{int(prvni_cislice)}{int(druha_cislice)}{int(treti_cislice)}{int(ctvrta_cislice)}")
print(nahodne_cislo)

#úvodní text
print("Hi there!")
print(oddelovac)
print("I've generated a random 4 digit number for you.\nLet's play a bulls and cows game")
print(oddelovac)

#začátek hry - zadání čísla, rozdělení na jednotlivé číslice do seznamu
zadane_cislo1 = input("Enter a number:")
#zajištění čtyřmístného čísla
if len(zadane_cislo1) == 4:
    print(oddelovac)
else:
    print("the number doesnt have four numbers")
    quit()
cislo1 = int(zadane_cislo1[0])
cislo2 = int(zadane_cislo1[1])
cislo3 = int(zadane_cislo1[2])
cislo4 = int(zadane_cislo1[3])
zadane_cislo1_seznam = list(f"{cislo1}{cislo2}{cislo3}{cislo4}")
print(zadane_cislo1_seznam)
cows_bulls = {"cows": 0, "buls": 0}
def kontrola_cisel(zadane_cislo1):
    for cislo in nahodne_cislo:
        if cislo in zadane_cislo1_seznam:
            cows_bulls["cows"] = +1
kontrola_cisel(zadane_cislo1)
print(cows_bulls)

#if zadane_cislo1 not in nahodne_cislo:
#   print("0 bulls, 0 cows")
#elif zadane_cislo1 in nahodne_cislo:
#   if zadane_cislo1[0] = nahodne_cislo[0]:
#    bulls
#for cislo in nahodne_cislo and zadane_cislo1_seznam


#každou číslici kontrolovat zvlášť tj. shodnost a pozici