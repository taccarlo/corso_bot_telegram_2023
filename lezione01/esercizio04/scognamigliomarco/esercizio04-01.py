lista = []
i=0
while i<5:
    val = input("inserisci una lettera: ")
    lista = lista + [val]
    i+=1
print (lista)

valoreUno = input("inserire lettera che vuoi sostituire: ")
valoreDue = input("inserire la lettera da inserire: ")

i=0
while i<5:
    if (lista[i] == valoreUno):
        lista[i] = valoreDue
    i+=1
print (lista)