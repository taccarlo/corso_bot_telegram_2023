print("Dite amici ed entrate")

for i in range(3):
    parola =input()
    
    if(parola!="amici") and (i<2):
             print ("Non succede nulla, ma sento una presenzache si avvicina")
    
    elif (parola!="amici") and (i==2):
             print ("Il mostro è qui, dobbiamo fuggire!")
             
    else:
        print ("Benvenuto a Moria")