def funzione2():

    s1 = input("E di bere qualcosa di caldo? ")
    risposta = s1.lower() #semplifico il controllo della stringa facendo diventare tutti i caratteri minuscoli
    
    if s1 == "si":
        scelta = input("Tè, Caffè o Cioccolata? ")
        risposta = scelta.lower() #semplifico il controllo della stringa facendo diventare tutti i caratteri minuscoli
        if risposta == "cioccolata":
            print("Fatevi sta", scelta)
        else:
            print("Fatevi sto", scelta)
        print("Siete diventati amici!")
        
    elif s1 == "no":
            print ("funzione3()") #inizio del codice di Marco
    else:
        print ("Rispondi con si o no") #in caso la risposta non sia si o no ripropongo la domanda
        funzione2()
funzione2()