def rossa():   
   int(input("Componi il numero di telefono: "))
   risposta = input("E' in casa? ")
   if risposta == "si":
        risposta2 = input("Ti va di manigare qualcosa assieme? ")
        if risposta2 == "si":
            print("Mangiate qualcosa assieme!")
            print("Siete diventati amici")
        elif risposta2 == "no":
            blu()
   elif risposta == "no":
        print("Lascia un messaggio e aspetta di essere chiamato.")

def blu():
    risposta3 = input("Hai voglia di bere qualcosa di caldo? ")

    if risposta3.lower() == "si":
        scelta = input("Cosa ti piacerebbe bere? Scegli tra tè, caffè o cioccolata: ")
        
        if scelta.lower() == "tè":
            print("Perfetto, andata per una bella tazza di tè caldo!")
        elif scelta.lower() == "caffè":
            print("Perfetto, andata per una bella tazza di caffè caldo!")
        elif scelta.lower() == "cioccolata":
            print("Perfetto, andata per una bella tazza di cioccolata calda!")
    elif risposta3.lower() == "no":
        verde()

def verde():
    print("Allora svaghiamoci un po'...")
    N = 0
    while N <= 6:
        domanda = input("...cosa ti va di fare? ")
        risposta4 = input("Ti va di farlo anche a te? ")
        if risposta4 == "s":
            print("Fatelo insieme, siete diventati amici")
            break
        else:
            N += 1
    if N > 6:
        print("Scegli fra tutte le opzioni quella meno disumana")
        print("Fattela piacere")
        print("Siete diventati amici")
rossa()