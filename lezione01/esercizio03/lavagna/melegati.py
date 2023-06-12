"""stringa “Dite amici ed entrate” e ci chiede di inserire 
una parola (che dovrebbe essere “amici”). Se sbagliamo il 
programma dovrà scrivere “Non succede nulla, ma sento una
 presenza che si avvicina” e dovrà chiederci nuovamente la 
 parola; se sbaglieremo ancora dovrà scrivere “Non succede 
 nulla, ma la presenza è molto vicina” e dovrà richiederci 
 la parola. Se sbagliamo per la terza volta scriverà 
 “Il mostro è qui, dobbiamo fuggire!” e poi il programma deve finire.
Se in qualsiasi momento inseriamo la parola “amici” 
il programma deve stampare “Benvenuti a Moria” e deve terminare."""
global tentativo
tentativo = 1
 
def Domanda():
    global tentativo

    parola = input ("INSERISCI UNA PAROLA")
    if ( parola != "amici"):
        if (tentativo < 3) :
            Sbagliato()
        else:
            print ("Il mostro è qui, dobbiamo fuggire!")
    
def Sbagliato():
    print("Non succede nulla, ma sento una presenza che si avvicina")
    global tentativo
    tentativo = tentativo + 1
    Domanda()


Domanda()