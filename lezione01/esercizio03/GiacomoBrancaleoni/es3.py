print("Dite amici ed entrate")
parola = input("Inserisci una parola: ")
if(parola == "amici"):
    print("Benvenuti a Moria.")
else:
    print("Non succede nulla, ma sento una presenza che si avvicina")
    parola = input("Inserisci una parola: ")
    if(parola == "amici"):
        print("Benvenuti a Moria.")
    else:
        print("Non succede nulla, ma la presenza è molto vicina")
        parola = input("Inserisci una parola: ")
        if(parola == "amici"):
            print("Benvenuti a Moria.")
        else:
            print("Il mostro è qui, dobbiamo fuggire!")