"""
Prendere in input una lista da tastiera e ritornare una lista che scambi le occorrenze di una lettera con un'altra.
"""
l = ['p', 'i', 'p', 'p', 'o']
for i in range(len(l)):
    if l[i] == 'p':
        l[i] = 'l'
print(l)

"""
Concatenare due liste prese da tastiera
"""
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

"""
Prendere in input una lista, la controlla 
e se contiene almeno un valore che non sia un intero ritorna un errore. 
Altrimenti dare in output una lista che in prima posizione contiene
il valore minimo dell'input, in seconda posizione la media e in terza posizione 
contiene il valore massimo.
"""
