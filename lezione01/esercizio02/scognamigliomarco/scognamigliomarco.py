# Vogliamo scrivere un programma che controlla se 
# due numeri inseriti dall’utente sono pari.

tentativoUno = int(input("inserisci il primo numero: "))
tentativoDue = int(input("inserisci il secondo numero: "))
if (tentativoUno %2 == 0):
    print (tentativoUno, "è pari")
else:
    print (tentativoUno, "è dispari")
if (tentativoDue %2 == 0):
    print (tentativoDue, "è pari")
else:
    print (tentativoDue, "è dispari")
