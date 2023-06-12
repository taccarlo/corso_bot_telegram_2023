print ("Dite amici ed entrate")
parola = str(input("inserire parola amici: "))
controllo = False
if (controllo == False and parola == "amici"):
    print ("Benvenuti a Moria")
    controllo = True
else :
    print ("Non succede nulla, ma sento una presenza che si avvicina")
if (controllo == False):
    parola = str(input("inserire parola amici: "))
    if (parola == "amici"):
        print ("Benvenuti a Moria")
        controllo = True
    else:
        print ("Non succede nulla, ma la presenza è molto vicina")
if (controllo == False):
    parola = str(input("inserire parola amici: "))
    if (parola == "amici"):
        print ("Benvenuti a Moria")
        controllo = True
    else:
        print ("Il mostro è qui, dobbiamo fuggire!")