'''
Prendere in input una lista da tastiera e ritornare una
lista che scambi le occorrenze di una lettera con un'altra.


lista=[]

i=0
while i<10:
    val= input('inserisci valore:')
    lista = lista+[val]
    i=i+1
    print ('Hai inserito ', lista)

print('finito!')'''

'''Concatenare due liste prese da tastiera'''

lista1 = [1, 2, 3]
lista2 = [4, 5, 6]

lista1.extend(lista2)

print(lista1)