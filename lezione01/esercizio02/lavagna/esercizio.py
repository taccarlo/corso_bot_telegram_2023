tentativo = input("Inserisci la password")
if(tentativo =="python123"):
    print("Password corretta!")
else:
    print("Password errata")

# Vogliamo scrivere un programma che controlla se 
# due numeri inseriti dall’utente sono pari.
tentativo1 = int(input ("Inserisci un numero "))
tentativo2 = int(input ("Inserisci un secondo numero "))

if (tentativo1 %2 == 0) and (tentativo2 %2 == 0):
    print("I due numeri sono pari")
else:
    print("Uno dei due numeri è dispari")      