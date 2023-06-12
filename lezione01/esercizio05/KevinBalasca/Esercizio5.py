nome=str(input("Inserisci il tuo nome: "))
cognome=str(input("Inserisci il tuo cognome: "))
print("Buonasera", nome, cognome, ", cosa posso fare per lei?" )


print()
print("*********************************************")
print()

numero=int(input("Inserisci un numero intero: "))
print("l'ultima cifra del numero inserito è:", numero%10)

    
print()
print("*********************************************")
print()

str1=str(input("Inserisci una stringa: "))
str2=str(input("Inserisci una stringa: "))

if(str1==str2):
    print("Le stringhe inserite sono uguali!")
else:
    print("Le stringhe inserite non sono uguali!")
