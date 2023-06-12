print("Dite amici ed entrate")

i=3

while(i<4 and i>0):
    parola=input("Inserisci la passsword: ")
    if(parola=="amici"):
        print("Benvenuti a Moria!")
        i=0
    elif(i==3 and parola!="amici"):
        print("Non succede nulla, ma sento una presenza che si avvicina")
        i-=1
    elif(i==2 and parola!="amici"):
        print("Non succede nulla, ma la presenza è molto vicina")
        i-=1
    elif(i==1 and parola!="amici"):
        print("Il mostro è qui, dobbiamo fuggire!")
        i-=1
