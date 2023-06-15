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
        print("Sono andato in pensione")
    else:
        funzione3()