"""
    Prendere in input una lista da tastiera e ritornare una
    lista che scambi le occorrenze di una lettera con un'altra.
    print(sostituisci(['p','i','p','p','o'],'p','l')) 
    >>> ['l','i','l','l','o'] 
    

l = ['p', 'i', 'p', 'p', 'o']
for i in range(len(l)):
    # replace hardik with shardul
    if l[i] == 'p':
        l[i] = 'l'
 
# print list
print(l)

    Concatenare due liste prese da tastiera

lista =[]
i=0
while i<4:
    val = input("Inserisci un valore: ")
    lista = lista + [val]
    i=i+1

lista2 =[]
i=0
while i<4:
    val = input("Inserisci un valore: ")
    lista2 = lista2 + [val]
    i=i+1

lista_unita = lista+lista2

print("liste unite: ",lista_unita)

    Prendere in input una lista, la controlla 
    e se contiene almeno un valore che non sia un intero ritorna un errore. 
    Altrimenti dare in output una lista che in prima posizione contiene
    il valore minimo dell'input, in seconda posizione la media e in terza posizione 
    contiene il valore massimo.
"""
lista =[]
i=0
while i<4:
    val = int(input("Inserisci un valore: "))
    lista = lista + [val]
    i=i+1
risultato = []

# metto in prima posizione nella lista "risultato" il valore minimo dell'input 

# metto in seconda posizione nella lista "risultato" la media
s = lista[0] + lista[1] + lista[2]+ lista[3]
m = s/4
risultato.append(m)
print(risultato)
# metto in terza posizione nella lista "risultato" il valore massimo della lista

