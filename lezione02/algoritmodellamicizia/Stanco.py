def rosso():   
    numero= input("inserisci numero di telefono")
    si=1
    no=0
    risposta=int(input("sei in casa? inserisci una risposta se si digitare 1 se no digitare 0"))
    if risposta==0:
        print("lascia un messaggio, aspetta una risposta")
    risposta2=int(print("ti va di mangiare qualcosa?"))
    if risposta2==1:
        print("mangiate qualcosa insieme, siete diventato amici! ora hai una persona in più a cui rompere le palle in caso di bisogno e viceversa")
    else:
        blu()
        
        

def blu():
    r=input("E di bere qualcosa di caldo?")
    while r!="si" and r!="no":
        r=input("E di bere qualcosa di caldo?")
    if (r=="si"):
        r=input("scegli cosa vuoi bere: tè, caffè, cioccolata")
        while(r!="tè" and r!="caffè" and r!="cioccolata"):
            r=input("scegli cosa vuoi bere: tè, caffè, cioccolata")
        if (r=="tè"):
            print("Fatevi sto tè")
        elif (r=="caffè"):
            print("Fatevi sto caffè")
        else:
            print ("Fatevi sta cioccolata")
        print("Siete diventati amici, hai una persona in più a cui poter rompere le palle in caso di bisongo e viceversa")
    else:
        parteVerde()


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
        print("Svagatevi un po' insieme!")




rosso()

print("Siete diventati amici! Ora hai una persona in più a cui poter rompere le palle in caso di bisogno e viceversa!")




        
