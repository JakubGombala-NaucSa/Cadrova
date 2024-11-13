# *****************************************
# ********** NEPOVINNE PARAMETRE **********
# *****************************************

# ******** Nepovinny parameter end ********
print("Ahoj", end=" ")
print("svet")

print("Ahoj", end="\n")
print("svet")
# Parameter end je defaultne nastaveny na \n a to je zaciatok noveho riadku
# Mozeme ho zmenit na hocico ine

# ******** Nepovinny parameter sep ********
print("Tento", "text", "je", "rozdeleny", "medzerami", sep=" ")
print("Tento", "text", "je", "rozdeleny", "pomlckami", sep="-")
# Parameter sep je defaultne nastaveny na medzeru
# Mozeme ho zmenit na hocico ine

# *****************************************
# *************** FOR CYKLY ***************
# *****************************************

# For cyklus sa pouziva na opakovanie bloku kodu
for i in range(5):
    print("Ahoj")

for i in range(5):
    print(i)

for i in range(2,5):
    print(i)

for i in range(2,10,2):
    print(i)

# Uloha 2.1
# Vytvorte program, ktorý si vypýta od užívateľa jeho meno (so správou aby užívateľ vedel čo má zadať) a následne vypíše toto meno.
meno = input("Meno ? ")
print("Ahoj", meno)

# Uloha 2.2
# Za pomoci for cyklu napíšte program ktorý do riadku vypíše prvých n čísel od jedna. 
cislo = input("Cislo ? ")
for i in range(int(cislo)): # int(cislo) prevedie text na cislo
    print(i+1, end=" ")
