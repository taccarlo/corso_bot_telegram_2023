
def programma1():
    nome = input("Come ti chiami?")
    print("Buonasera ", nome, " cosa posso fare per te?")


"""
Scrivere un programma che legge il vostro nome e stampa 
“Buonasera [vostro nome e cognome], cosa posso fare per te?”
"""
#programma1()

def programma2():
    ultimaCifra = int(input("Inserisci un numero"))
    print("L'ultima cifra è ", ultimaCifra%10)
"""
Leggere un numero in input e stamparne l'ultima cifra.
"""
#programma2()

def programma3():
    stringa1 = input("Inserire la prima stringa.")
    stringa2 = input("Inserire la seconda stringa.")
    if(stringa1 == stringa2):
        print("Le stringhe sono uguali")
    else:
        print("Le stringhe non sono uguali")

"""
Leggere due stringhe da terminale e controllare se sono uguali
"""
programma3()