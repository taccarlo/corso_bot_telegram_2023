
#Prendere in input una lista da tastiera e ritornare una
#lista che scambi le occorrenze di una lettera con un'altra.

#Concatenare due liste prese da tastiera

#prima lista
lista1=[]
i=0

while i<10:
    val=input("inserire qualcosa: ")
    lista1.append(val)
    i=i+1
print("hai inserito: ",lista1)

#seconda lista
lista2=[]
i=0

while i<10:
    val=input("inserire qualcosa: ")
    lista2.append(val)
    i=i+1
print("hai inserito: ",lista2)

listaunita=lista1+lista2
print(listaunita)



#Prendere in input una lista, la controlla 
#e se contiene almeno un valore che non sia un intero ritorna un errore. 
#Altrimenti dare in output una lista che in prima posizione contiene
#il valore minimo dell’input, in seconda posizione la media e in terza posizione 
#contiene il valore massimo.

lista1=[]
i=0

while i<4:
    val=input("inserire qualcosa: ")
    lista1.append(val)
    i=i+1
risultato=[]

