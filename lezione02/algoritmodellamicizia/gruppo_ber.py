def funzione2():

    s1 = input("E di bere qualcosa di caldo? ")
    risposta = s1.lower()
    
    if s1 == "si":
        scelta = input("Tè, Caffè o Cioccolata? ")
        risposta = scelta.lower()
        if risposta == "cioccolata":
            print("Fatevi sta", scelta)
        else:
            print("Fatevi sto", scelta)
    else:
        funzione3()
funzione2()