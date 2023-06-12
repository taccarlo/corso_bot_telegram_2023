
parola = (input("inserisci una parola\n" ))
lista = []
i = 0
while i < len(parola)-1:
    lista[i] = parola[i]
    i+=1

lettera = (input("inserisci una lettera che vuoi cambiare\n"))
NewLettera = (input("inserisci la lettera con cui vuoi scambiare\n"))
j = 0
while i < len(parola):
    if lista[j] == lettera:
        lista[j] = (NewLettera)
    j+=1

print(lista)