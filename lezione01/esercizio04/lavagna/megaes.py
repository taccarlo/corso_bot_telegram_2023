
lista=[]
lista2=[]

i=0 
min=0
s=0
max=0
while i<4:
    val= input ("inserisci un valore")
    lista= lista + [val]
    i= i+1
    s= s+ val
    if [val]<min:
        min=[val]
    if [val]>max:
        max=[val]

    print ("Hai inserito", lista)


print (lista2[min, s%i, max])
