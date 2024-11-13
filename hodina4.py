# *****************************************
# ************* PODMIENKY - IF ************
# *****************************************

cislo = 5
if (cislo == 5 ): # POZOR je rozdiel medzi = a ==
    print( "číslo = 5" ) 

slovo = input( "zadajte slovo: " )
if slovo == "auto" :
    print( "zadané slovo je 'auto'" )
else :
    print( "zadané slovo nie je 'auto'" ) 

slovo = input("Zadaj slovo: ")
if slovo == "matika":
    print("pssst, toto meno sa nesmie vypisovat")
    
# *****************************************
# ************ LOGICKE OPERATOTY **********
# *****************************************

# a < 50    je true (pravda), ak a (premenná) je menšie ako 50
# a <= 50   je true, ak a je menšie alebo rovné ako 50
# a >= 50   je true, ak a je väčšie alebo rovné ako 50
# a == 50   je true, ak a je rovné 50
# a != 50   je true, ak a nerovná sa 50 

# Uloha 4.1
# Napíšte program, ktorý si od užívateľa vypýta slovo, uloží ho do premennej. 
# Ak je slovo „voldemort“, vypíše „psst toto meno nesmieme vypisovať“. 
slovo = input("Zadaj slovo: ")
if slovo == "voldemort":
    print("psst toto meno nesmieme vypisovat")

# Uloha 4.2
# Napíšte program, ktorý si od užívateľa vypýta dve slová (napríklad zadajte nové heslo a zopakujte heslo) 
# ak sú slová rozdielne, vypíše „Heslá musia byť rovnaké“ 

slovo1 = input("Zadaj slovo1: ")
slovo2 = input("Zadaj slovo2: ")
if slovo1 != slovo2:
    print("Hesla musia byt rovnake")