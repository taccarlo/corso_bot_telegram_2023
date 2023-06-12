def Stampa():
    print("Il tuo numero è tra i seguenti?")
    i = 0

    list=[]
    for x in range(8, 63):
        if(i<8):
            list.append(x)
            i += 1
        elif(i < 15):
            i += 1
        else:
            i=0
    print(list)
        
    

