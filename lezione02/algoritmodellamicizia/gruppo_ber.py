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
        


funzione3()