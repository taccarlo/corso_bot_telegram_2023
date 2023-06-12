def primo():
    print("Il tuo numero è tra i seguenti?")
    list=[]
    for i in range(2, 62, 4):
        list.append(i)
        list=list+[i+1]
    print(list," ")
