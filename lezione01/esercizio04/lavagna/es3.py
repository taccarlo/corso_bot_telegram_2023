lista=[]
i=0 
c=0
while i<10:
    val= input ("inserisci un valore")
    lista= lista + [val]
    i= i+1
    print ("Hai inserito", lista)

    if type([val])!=int:
        c=c+1

if i==10 & c!=0:
    print ("Error")