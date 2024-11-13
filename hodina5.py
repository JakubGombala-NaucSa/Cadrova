# *****************************************
# ************HRA UHADNI CISLO ************
# *****************************************

from random import randint
cislo = randint(1,10)

for i in range(3):
    pokus = input("Hadaj cislo: ")
    if int(pokus) == cislo:
        print("Vyhral si")
        break
    elif int(pokus) > cislo:
        print("Nespravne")
        print("Hadane cislo je mensie")
    else:
        print("Nespravne")
        print("Hadane cislo je vacsie")





