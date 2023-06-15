listaUno = []
i=0
while i<5:
    val = input("inserisci una lettera: ")
    listaUno = listaUno + [val]
    i+=1

listaDue = []
i=0
while i<5:
    val = input("inserisci una lettera: ")
    listaDue = listaDue + [val]
    i+=1

listaTot = (listaUno + listaDue)
print (listaTot)