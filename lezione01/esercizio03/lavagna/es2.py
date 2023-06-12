print ("Dite amici ed entrate")

for i in range(3):
    parola=input()

    if (parola!="amici" & i<2):
        print("Non succede nulla, ma sento una presenza che si avvicina")  

    elif (parola!="amici" & i==2):
        print("Il mostro è qui, dobbiamo fuggire!")  

    else:
        print("Benvenuti a Moria")
        break