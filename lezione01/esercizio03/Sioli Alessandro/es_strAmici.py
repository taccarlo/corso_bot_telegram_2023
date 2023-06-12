s1 = ""
i = 0

while (s1 != "amici" and i < 3) :
    s1 = input ("Dite amici ed entrate ")

    if (s1 != "amici" and i == 0) :
        print ("Non succede nulla, ma sento una presenza che si avvicina")
    elif (s1 != "amici" and i == 1) :
        print ("Non succede nulla, ma la presenza è molto vicina")
    elif (s1 != "amici" and i == 2) :
        print ("Il mostro è qui, dobbiamo fuggire!")
    else :
        print ("Benvenuti a Moria")
    i = i + 1
