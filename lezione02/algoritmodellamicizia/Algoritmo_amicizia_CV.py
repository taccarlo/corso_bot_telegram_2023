#Rosso#
def rosso():   
    numero= input("inserisci numero di telefono")
    si=1
    no=0
    risposta=int(input("sei in casa? inserisci una risposta se si digitare 1 se no digitare 0"))
    if risposta==no:
        print("lascia un messaggio, aspetta una risposta")
    risposta2=int(input("ti va di mangiare qualcosa?"))
    if risposta2==si:
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
        blocco_verde()


def blocco_verde():
    global no
    if no == 0:
        no_caldo()    
    if no > 6:
        tante_prop()
    if no < 6 and no > 0 :
        no_prop()
        global o
        if o == "SI" or o == "si" or o == "Si" or o == "sì" or o == "Sì":
            amicizia()
        else:
            p = input("Proponi qualcosa ")
            no = no + 1
            if no > 6:
                tante_prop()
            else:
                no_prop()
            
def no_caldo():
    global n
    f = 0
    f = input("Allora svaghiamoci un po', cosa ti va di fare?")
    no = no + len(f)
def tante_prop():
    print("Ok, scegli la meno disumana, svagatevi un po' eeeeeeeeeeeeee...")
    amicizia()
def no_prop():
    o = input("Va bene la mia proposta?")
    if(o=="no"):
        blocco_verde()
    else:
        amicizia()

def amicizia():
    print("Adesso siete amici!!!")
    return
    
rosso()