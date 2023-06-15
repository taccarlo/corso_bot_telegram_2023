
# Dati tre numeri identificare il minimo e il massimo
numero1=int(input("inserisci un numero"))
numero2= int(input("inserisci un numero"))
numero3= int(input("inserisci un numero"))

massimo=numero1
if(massimo<numero2):
    massimo=numero2
elif(massimo<numero3):
    massimo=numero3
print("il numero massimo è:", massimo)

minimo=numero1
if(minimo>numero2):
    minimo=numero2
elif(minimo>numero3):
    minimo=numero3
print("il numero minimo è:", minimo)