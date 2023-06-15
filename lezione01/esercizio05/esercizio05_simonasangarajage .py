'''Scrivere un programma che legge il vostro nome e stampa 
“Buonasera [vostro nome e cognome], cosa posso fare per te?”

Leggere un numero in input e stamparne l’ultima cifra.

Leggere due stringhe da terminale e controllare se sono uguali'''
def stampa_nome():
    n=input('inserisci il tuo nome :')
    print ('Buonasera', n , 'cosa posso far per te ?')

'---------------------------------------------------------'
def numero ():
    num = input ('inserisci un numero di almeno due cifre:')
    ultima_cifra = int(num[-1])
    print (ultima_cifra)
'_________________________________________________________'

def compara_stringhe ():
    str1=input('inserisci una stringa :')
    str2=input ('inserisci un\'altra stringa:')
    if (str1==str2):
        print('uguali')
    else:
        print('diverse')
    
