lista = [] 
valoreUno = str(input("inserisci la lettera che vuoi cambiare "))
valoreDue = str(input("inserisci la lettera "))

i = 0

while i<10:
    lettera = input("inserisci una lettera ")
    lista = lista + [lettera]
    i += 1

d = 0

while d<10:
    if (lista[d] == valoreUno):
        lista[d] = valoreDue
    d += 1
print(lista)