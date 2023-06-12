lista1 =[]
i=0
while i<5:
    val = input("Inserisci un valore: ")
    lista1 = lista1 + [val]
    i=i+1
lista2 =[]
l = 0
while l<5:
    val = input("Inserisci un valore: ")
    lista2 = lista2 + [val]
    l=l+1
lista = lista1 + lista2
print("Hai inserito: ",lista)