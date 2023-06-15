numero=int(input("Inserisci un numero: "))
if(numero%2==0):
    print("Il numero inserito è pari!")
else:
    print("Il numero inserito è dispari!")
    numero=int(input("Inserisci un numero: "))
    if(numero%2==0):
        print("Primo numero inserito dispari, secondo pari!")
    else:
        print("Entrambi i numeri inseriti sono dispari!")


print()
print("************************************************************")
print()


numero1=int(input("Inserisci un numero: "))
numero2=int(input("Inserisci un numero: "))
numero3=int(input("Inserisci un numero: "))

if(numero1>numero2 and numero1>numero3):
    print(numero1, "è il maggiore")
    if(numero2>numero3):
        print(numero3, "è il minore")
    else:
        print(numero2, "è il minore")
elif(numero2>numero1 and numero2>numero3):
    print(numero2, "è il maggiore")
    if(numero1>numero3):
        print(numero3, "è il minore")
    else:
        print(numero1, "è il minore")
elif(numero3>numero1 and numero3>numero3):
    print(numero3, "è il maggiore")
    if(numero1>numero2):
        print(numero2, "è il minore")
    else:
        print(numero1, "è il minore")


print()
print("************************************************************")
print()


numero=int(input("Inserisc un numero: "))
print(abs(numero))
if(numero<0):
    print(numero*-1)
else:
    print(numero)


print()
print("************************************************************")
print()

primo=True
numero=int(input("Inserisci un numero: "))
while(numero<1 or numero>5):
    numero=int(input("Inserisci un numero: "))

for i in range(2,numero):
    if(numero%i==0):
        primo=False

if(primo):
    print(numero, "è primo")
else:
    print(numero, "non è primo")




























