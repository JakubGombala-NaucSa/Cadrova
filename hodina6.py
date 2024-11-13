# *****************************************
# **************** FUNKCIE **************** 
# *****************************************

# def ako define (definovat)
def funkcia():
    print("Zaciatok funkcie")
    print("Koniec funkcie")

print("Prve volanie funkcie")
funkcia()
print("druhe volanie funkcie")
funkcia()
print("tretie volanie funkcie")
funkcia()

def scitaj(cislo1, cislo2):
    print(cislo1 + cislo2)

a = input("Napis cislo1: ")
b = input("Napis cislo2: ")

scitaj(2, 2)
scitaj(int(a), int(b))

# Uloha 5.1
# Napíšte funkciu pozdrav(meno) ktorej pošlete jeden parameter, meno, a ona ho pozdraví. 
def pozdrav(meno):
    print("Ahoj", meno)
    
pozdrav("Tadeas")
pozdrav("Petra")
pozdrav("Malina")

# Uloha 5.2
# Napíšte funkciu opakuj(slovo, pocet) ktorej pošlete dva parametre, nejaké slovo a koľko krát sa má vypísať
def opakuj(slovo, pocet):
    for i in range(pocet):
        print(slovo)

opakuj("Dvere", 30)



















