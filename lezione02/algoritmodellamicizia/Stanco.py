def rosso():   
    numero= input("inserisci numero di telefono")
    si=1
    no=0
    risposta=int(input("sei in casa? inserisci una risposta se si digitare 1 se no digitare 0"))
    if risposta==1:
        print("ti va di mangiare qualcosa insieme?")
        if risposta==1:
            print("mangiate qualcosa")
        else:      
    else:
        print("lascia un messaggio")




def parteVerde():
    n=0
    proposte=[]
    print("Allora svaghiamoci un po'!")
    while(n<7):
        if(n<7):
            proposta=input("Cos'altro ti va di fare? ")
            proposte.append(proposta)
            rsposta=input("Vuoi farla anche tu? si/no")
                if(risposta=="si"):
                    print("E' facciamolo insieme!")
                    print("Svatevi un po' insieme")
                    break
                elif(risposta="no"):
                    n=n+1
    if(n>=5):                
        print(proposte)
        scelta=input("Scegli fra tutte le opzioni quella che ti appare meno disumana")
        print("Svagatevi un po' insieme")
