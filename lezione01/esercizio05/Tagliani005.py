nome = input("inserire nome: ")
cognome = input("inserire cognome: ")

print("buonsera ", nome, cognome, ", cosa posso fare per te?")

print("***********************************************************")

a = int(input("inserire numero: "))
a=a%10
print("l'ultima cifra è: ", a)

print("***********************************************************")

s1 = input("inserire stringa 1 : ")
s2 = input("inserire stringa 2 : ")
if(s1 == s2):
    print("stringhe uguali !!")
else:
    print("stringhe non uguali !!")
