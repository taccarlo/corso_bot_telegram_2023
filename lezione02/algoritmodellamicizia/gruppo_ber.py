def funzione3():
    n = 0
    print("allora svaghiamoci un po'...")
    while (n <6 ):
        print("...cos'altro ti va di fare?")
        risposta = int(input("è una cosa che va di fare anche a me? (rispondi 1 per sì e 0 per il no)"))
        if (risposta == 1):
            break
        else:
            n += 1
    if (risposta == 1):
        print("e facciamolo insieme, dai...")
    else:
        print("scegli fra tutte le opzioni quella che ti appare meno disumana", "\n", "fattela piacere")
    print("svagatevi un po' insieme", "\n")
    print("SIETE DIVENTATI AMICI! ora hai una persona in più a cui poter rompere le palle in caso di bisogno. e viceversa")


def funzione2():

    s1 = input("E di bere qualcosa di caldo? ")
    risposta = s1.lower() #semplifico il controllo della stringa facendo diventare tutti i caratteri minuscoli
    
    if s1 == "si":
        scelta = input("Tè, Caffè o Cioccolata? ")
        risposta = scelta.lower() #semplifico il controllo della stringa facendo diventare tutti i caratteri minuscoli
        if risposta == "cioccolata":
            print("Fatevi sta", scelta)
        else:
            print("Fatevi sto", scelta)
        print("Siete diventati amici!")
        
    elif s1 == "no":
            funzione3()#inizio del codice di Marco
    else:
        print ("Rispondi con si o no") #in caso la risposta non sia si o no ripropongo la domanda
        funzione2()

def inCasa(aCasa):
    if(aCasa == 1):
        mangiare()
    else:
        print("L'ascia un messaggio.")
        print("Aspetta di essere richiamato")
        mangiare()
    
def mangiare():
    risposta = str(input("Ti va di andare a mangiare qualcosa insieme?\n"))
    if(risposta == 1):
        print("Siete diventati amici!!")
    else:
        funzione2()#chiamata della seconda funzione in caso no

print("Compongo il numero di telefono")
inCasa(str(input("A casa?\n1 per si e 0 per no") ) )
