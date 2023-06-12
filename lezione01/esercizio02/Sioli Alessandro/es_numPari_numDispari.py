n1 = input("Inserisci un numero ")
n2 = input("Inserisci un altro numero ")
n1 = int(n1)
n2 = int(n2)

if (n1 % 2 + n2 % 2 == 0) :
    print ("Entrambi i numeri sono pari")
elif (n1 % 2 + n2 % 2 == 2) :
    print ("Entrambi i numeri sono dispari")
elif (n1 % 2 == 0) :
    print ("Solo il primo numero è pari")
else:
    print ("Solo il secondo numero è pari")