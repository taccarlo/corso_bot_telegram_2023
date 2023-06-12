lista1 = []
lista2 = []
i = 0

while i < 5 :
    n = input ("Inserire un valore da immettere nella prima lista ")
    lista1 = lista1 + [n]
    if type(lista1[i]) == int :
        print ("errore")
        break
    i = i + 1
    
i = 0
while i < 5 :
    n = input ("Inserire un valore da immettere nella seconda lista ")
    lista2 = lista2 + [n]
    i = i + 1

print (lista1 + lista2)
