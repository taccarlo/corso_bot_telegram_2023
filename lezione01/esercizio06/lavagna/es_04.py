
# Scrivere un programma che legge un numero compreso
# tra 1 e 5 e controlla se è primo.

n=int(input("inserire numero: "))
if n>=1 and n<=5:
    div=2
    contatore=0
    while div<=n/2 and contatore==0:
        if n%div==0:
            contatore+=1
        div+=1
    if contatore==0:
        print("il numero è primo")
    else:
        print("il numero non è primo")
else:
    print("il numero dave essere compreso tra 1 a 5")
