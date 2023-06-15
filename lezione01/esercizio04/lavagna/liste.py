risposta = input("Hai voglia di bere qualcosa di caldo? ")

if risposta.lower() == "si":
    scelta = input("Cosa ti piacerebbe bere? Scegli tra tè, caffè o cioccolata: ")
    
    if scelta.lower() == "tè":
        print("Perfetto, andata per una bella tazza di tè caldo!")
    elif scelta.lower() == "caffè":
        print("Perfetto, andata per una bella tazza di caffè caldo!")
    elif scelta.lower() == "cioccolata":
        print("Perfetto, andata per una bella tazza di cioccolata calda!")

    