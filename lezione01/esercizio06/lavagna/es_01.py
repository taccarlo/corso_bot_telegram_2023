"""
Leggere un numero da terminale e controllare se è pari;
se lo è stampate “pari” a terminale, altrimenti leggete un secondo numero.
Se il secondo numero è dispari stampate “entrambi dispari”, 
altrimenti stampate “primo dispari, secondo pari”
"""

numero1 = int(input("dammi il primo numero\n"))
numero2 = int(input("dammi il secondo numero\n"))
if (numero1%2==0):
    print (numero1)
elif (numero2%2==1 and numero1%2==1):
    print("sono entrambi dispari")
else:
    print("il primo è pari e il secondo è dispari")