# *****************************************
# ******** PÍSANIE KÓDU DO BLOKOV *********
# *****************************************

for i in range( 10 ):
    print("Tento kód je sucast cyklu")
    print("Tento kód je tiez sucast cyklu") 

for i in range( 10 ):
    print( "Tento kód sa opakuje" )
print( "Tento kód sa už neopakuje" ) 


sucet = 0

for i in range(1,1000000000001):
    sucet = sucet + i
print(sucet)

# Uloha 3.1
# Napíšte program, ktorý si vypýta od užívateľa dve slová (musíte dvakrát použiť príkaz input) 
# vypíše ich 5 krát, potom vypíše reťazec „medzera medzi for cyklami“ n
# následne zadané slová vypíše ešte 5 krát.

slovo1 = input("Napis slovo1: ")
slovo2 = input("Napis slovo2: ")
for i in range(5):
    print(slovo1)
    print(slovo2)
print("medzera medzi for cyklami")
for i in range(5):
    print(slovo1)
    print(slovo2)

# uloha 3.2
# Napíšte for cyklus, ktorý si v každej iterácii vypýta od užívateľa slovo a následne ho vypíše.
# For cyklus môže bežať ľubovoľne veľa krát. 

for i in range(5):
    slovo = input("Napis slovo: ")
    print(slovo)


# ********************************************
# * VYUŽÍVANIE RIADIACEJ PREMENNEJ FOR CYKLU *
# ********************************************

suma = 0
for i in range( 10 ):
    suma = suma + i
print(suma)

for i in range(0, 11, 2):
    print(i)

# Uloha 3.3
# Napíšte for cyklus, ktorý vypíše všetky nepárne čísla od 0 po 10

for i in range(1, 11, 2):
    print(i)

# Uloha 3.4
# Napíšte for cyklus, ktorý vynásobí všetky čísla od 1 po 10 a vypíše tento výsledok 
sucin = 1
for i in range(1, 11):
    sucin = sucin * i
print(sucin)

