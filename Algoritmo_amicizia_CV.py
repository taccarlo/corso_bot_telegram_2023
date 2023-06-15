#Rosso#

n = 0
o = ''
#blu#


#verde#
def no_caldo():
    global n
    f = 0
    f = input("Allora svaghiamoci un po', cosa ti va di fare?")
    n = n + len(f)
def tante_prop():
    print("Ok, scegli la meno disumana, svagatevi un po' eeeeeeeeeeeeee...")
    amicizia()
def no_prop():
    o = input("Va bene la mia proposta?")
def blocco_verde():
    global n
    if n == 0:
        no_caldo()    
   
    if n > 6:
         tante_prop()
    
    if n < 6 and n > 0 :
        no_prop()
        global o
        if o == "SI" or o == "si" or o == "Si" or o == "sì" or o == "Sì":
            amicizia()
        else:
            p = input("Proponi qualcosa ")
            n = n + 1
            if n > 6:
                tante_prop()
            else:
                no_prop()
            
        
def amicizia():
    print("Adesso siete amici!!!")
    return
blocco_verde()