nomeCognome = ["Matteo", "Marcologo"]

print("Buonasera",nomeCognome[0],nomeCognome[1])

# secondo programma #

numero = input("inserire un numero: ")
numero = int(numero)

print("L'ultima cifra del numero è: ",numero % 10)

# terzo programma #

s1 = input("Inserire una stringa: ")
s2 = input("Inserire una stringa: ")

if(s1 == s2):
    print("Le stringhe sono uguali", s1, " uguale a",s2)
else:
    print("Le stringhe non sono uguali", s1, " è diverso da",s2)
