Primo_numero= input ("Inserire valore ")
Secondo_numero= input ("Inserire valore ")
Primo_numero=int(Primo_numero)
Secondo_numero=int(Secondo_numero)


if(Primo_numero%2==0 & Secondo_numero%2==0 ):
    print ("Entrambi i numeri sono pari")


if(Primo_numero%2!=0 & Secondo_numero%2!=0 ):
    print ("Entrambi i numeri sono dispari")


if(Primo_numero%2!=0 & Secondo_numero%2==0 ):
    print ("Solo il secondo numero è pari")

if(Primo_numero%2==0 & Secondo_numero%2!=0 ):
    print("Solo il primo numero è pari")