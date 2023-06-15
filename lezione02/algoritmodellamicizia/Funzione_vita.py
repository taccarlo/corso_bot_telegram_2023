"""def funzione_2():
    a==1
    while a<20:
        a+=1
        print("questo è il tuo", a,"anno di servizio")
        i=input("ti sei infortunato?")
        if i == ("S") or i == ("s"):
        funzione_2()"""
def funzione_1(): 
    print("Sei nato!!")
    print("Esegui elementari e medie")
    bocciature = 0
    anno_superiori = 0
    while bocciature <3 and anno_superiori <5:
        print("Sei al ", anno_superiori + 1, "anno di superiori")
        d = input("sei stato bocciato? ")
        if d == ("s") or d == ("S"):
            bocciature +=1
        else:
            anno_superiori +=1
    funzione_2()
funzione_1()

