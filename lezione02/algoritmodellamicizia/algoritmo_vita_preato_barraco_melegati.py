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
def funzione_2():
    c = 0
    b = 0
    while c < 20:
        c += 1
        i= input("Infortunio? ")
        if i == "S" or i == "s":
            print("Pensione")
            b +=1
        else:
            i= input("Infortunio? ")
            c +=1
            if i == "S" or i == "s":
                print("Pensione")
                b += 1
                break
    if b == 0:
        pensione()

def pensione():
    print ("Ultimi anni di lavoro.")
    dod = int(input("Quante promozioni? "))
    if dod <= 3:
        print("Pensione")
    if dod > 3:
        print ("Capo azienda")
        print("Pensione")
funzione_1()
    