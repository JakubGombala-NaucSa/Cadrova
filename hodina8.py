def sucet(a, b):
    # return vracia ale nevypisuje
    return a + b # return ukoncuje funkciu
    
premenna = sucet(sucet(9,8),5)

##print(premenna)

def je_parne(cislo):
    if cislo % 2 == 0:
        return str(cislo) + " je parne"
    return str(cislo) + " je neparne"

##for i in range(100):
##    print(je_parne(i))
    
def vylepsi(slovo):
    return slovo + " je super!"

##print(vylepsi("Pes"))

def je_pravouhly(alfa, beta, gama):
    if alfa + beta + gama != 180:
        return False
    if alfa == 90 or beta == 90 or gama == 90:
        return True
    return False

def obsah_trojuholnika(a, b, alfa, beta, gama):
    if je_pravouhly(alfa, beta, gama):
        return a * b / 2
    return 0

##print(obsah_trojuholnika(4,2,90,45,45))
##print(obsah_trojuholnika(4,2,90,145,45))
##print(obsah_trojuholnika(4,12,90,30,60))
 
print("Ahoj" + "Cau")
print("Ahoj " * 7)
text = "Ahoj ako sa mas ?"
print(len(text))













    
