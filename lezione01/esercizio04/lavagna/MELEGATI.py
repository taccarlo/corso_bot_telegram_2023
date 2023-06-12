"""Prendere in input una lista da tastiera e ritornare una
lista che scambi le occorrenze di una lettera con un'altra.
"""
lista=[]
i =0
while i<10:
  lett= input("inserisci lettera: ")
  lista = lista + [lett]
  i = i + 1
print ("lista 1", lista)
for i in range (len(lista)):
    if lista[i]== 'j':
        lista[i]= 'k'
print ("lista corretta", lista)