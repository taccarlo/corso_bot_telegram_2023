print("Dite amici ed entrate")
p=input("inserisci la parola: " )

if (p!="amici"):
    print("Non succede nulla, ma sento una presenza che si avvicina")
    p=input("inserisci la parola: " )
    if (p!="amici"):
        print("Non succede nulla, ma la presenza è molto vicina")
        p=input("inserisci la parola: " )
    if (p!="amici"):
        print("Il mostro è qui, dobbiamo fuggire!")
elif (p=="amici"):
    print("Benvenuti a Moria")

    
   
