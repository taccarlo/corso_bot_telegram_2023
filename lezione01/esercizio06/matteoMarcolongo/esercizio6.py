n = int(input("Inserire un numero: ") )
n2 = int(input("Inserire un numero: ") )

if(n % 2 == 0):
    print("Il primo numero è pari")
elif(n2 % 2 == 0):
    print("Il secondo numero è dispari")
elif(n % 2 == 0 and n2 % 2 == 0):
    print("Sono entrambi pari")
elif(n % 2 != 0 and n2 % 2 != 0):
    print ("Sono entrambi dispari")

# secondo programma #

o = []
i = 0
while i0<3:
    numero = input("Inserire un numero: ")
    o = o + [numero]
    i =+ 1

if(n[0] < n[1] and n[0] < n[2]):
    print("Il primo numero è il più grande")
elif (n[1] < n[0] and n[1] < n[2]):
    print("Il secondo numero è il più grande")
else:
    print("Il terzo numero è il più grande")

# terzo programma #



# quarto programma #

p = input("Inserire un numero compreso tra 1 e 5: ")

if(p <= 5 and p >= 1 and p % 2 == 0):
    if(p == 2):
        print("è un numero primo")
    else:
        print("Non è un numero ")
    
else:
    print("è un numero primo: ")
