print("Dite amici ed entrate")
for i in range (3):
    parola = input()
    if (parola != "amici") and (i<2):
        print("non succede nulla ma la presenza si avvicina")
    elif (parola != "amici") and (i==2):
     print("il mostro si avvicina bro scappa")
    else:
        print("Benvenuto bro")
        break

    
