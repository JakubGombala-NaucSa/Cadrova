def opakuj(slovo, pocet):
    # Tato funkcia vypise slovo
    # pocet krat
    for i in range(pocet):
        print(slovo)

##opakuj("Ahoj", 3)
##opakuj("nazdar", 7)

# Funkcia s nazvom poradie a
# parametrom n
def poradie(n):
    # Vypise vsetky cisla
    # od 1 po n
    for i in range(n):
        print(i+1)
        
# Funkcia s nazvom poradie a
# parametrom n
def poradie2(n):
    # Vypise vsetky cisla
    # od 1 po n
    for i in range(1, n+1):
        print(i)

##poradie(5)
##poradie2(5)

def stvorec(n):
    for i in range(n):
        print("*"*n)

def stvorec2(n):
    for i in range(n):
        for j in range(n):
            print("*", end="")
        print()

def stvorec3(n, pismenko):
    for i in range(n):
        print(pismenko*n)

##stvorec(5)  
##stvorec2(2)
##stvorec(12)

##stvorec(2)
##stvorec3(2, "A")
##stvorec3(2, "B")
##stvorec3(2, "X")
##
##stvorec3(5, "Jakub")

def obvod_stvorca(a):
    return a*4

obvod = obvod_stvorca(7)
print(obvod)




    
