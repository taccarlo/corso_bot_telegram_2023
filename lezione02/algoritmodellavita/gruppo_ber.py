def funzione3():
    print("ultimi anni di lavoro")
    promozioni = int(input("quante promozioni? "))
    if (promozioni > 3):
        print("capo di azienda")
    else:
        print("PENSIONE")


def funzione2():
    print ("Inizio a lavorare")
    i = 0
    infortunio = bool(False)
    while i < 20 and infortunio == False:
        i += 1
        print("Ho completato il %d anno di lavoro" %i)
        j = input("Mi sono infortunato? ")
        j.lower()
        if j == "si":
            infortunio = True
        
    if infortunio:
        print("PENSIONE")
    else:
        funzione3()

def funzione1():
    annoSuperiori = 0
    bocciature = 0 # numero di bocciature

    print("La persona è nata.")
    print("Seguo l'anno %s anno delle superiori" % annoSuperiori)
    while annoSuperiori < 5 and bocciature < 3:

        print("Seguo l'anno %s anno delle superiori e sono stato bocciato %s volte" % (annoSuperiori, bocciature))
        bocciato = int(input("bocciato\n1 si 0 no\n") ) # se è stato bocciato si o no

        if bocciato == 1:

            bocciature+=1
            print("Seguo l'anno %s anno delle superiori e sono stato bocciato %s volte" % (annoSuperiori, bocciature))

            if bocciature > 3:
                funzione2

        else:
            annoSuperiori+=1
    funzione2

funzione1()