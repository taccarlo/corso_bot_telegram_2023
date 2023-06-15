def blu():
    r=input("E di bere qualcosa di caldo?")
    while r!="si" and r!="no":
        r=input("E di bere qualcosa di caldo?")
    if (r=="si"):
        r=input("scegli cosa vuoi bere: tè, caffè, cioccolata")
        while(r!="tè" and r!="caffè" and r!="cioccolata"):
            r=input("scegli cosa vuoi bere: tè, caffè, cioccolata")
        if (r=="tè"):
            print("Fatevi sto tè")
        elif (r=="caffè"):
            print("Fatevi sto caffè")
        else:
            print ("Fatevi sta cioccolata")
        print("Siete diventati amici, hai una persona in più a cui poter rompere le palle in caso di bisongo e viceversa")
