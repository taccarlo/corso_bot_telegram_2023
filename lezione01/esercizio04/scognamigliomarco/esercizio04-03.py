lista = []
i=0
while i<5:
    val = int(input("inserisci un numero: "))
    lista = lista + [val]
    i+=1
print (lista)

controllo = True
i=0
valoreminimo = lista[0]
valoremedia = 0
valoremassimo = lista[0]
while i<5:
    if (type[lista[i]] != int ):
        print ("ERRORE")
        controllo = False
        break
    else:
        if (valoreminimo > lista[i]):
            valoreminiomo = lista[i]
        valoremedia += lista[i]
        if (valoremassimo < lista[i]):
            valoremassimo = lista[i]
valoremedia = valoremedia/5

if (controllo == True):
    listaTot[valoreminimo, valoremedia, valoremassimo]
    print (listaTot)