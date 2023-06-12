'''
Scriviamo un programma che per prima cosa stampa la 
stringa “Dite amici ed entrate” e ci chiede di inserire 
una parola (che dovrebbe essere “amici”). Se sbagliamo il 
programma dovrà scrivere “Non succede nulla, ma sento una
 presenza che si avvicina” e dovrà chiederci nuovamente la 
 parola; se sbaglieremo ancora dovrà scrivere “Non succede 
 nulla, ma la presenza è molto vicina” e dovrà richiederci 
 la parola. Se sbagliamo per la terza volta scriverà 
 “Il mostro è qui, dobbiamo fuggire!” e poi il programma deve finire.
Se in qualsiasi momento inseriamo la parola “amici” 
il programma deve stampare “Benvenuti a Moria” e deve terminare.
'''


print ('Dite amici ed entrate')

parola = input('inserisci una parola:')

if (parola=='amici'):
    print ('benvenuti a moria')
elif (parola!= 'amici'):
    print('Non succede nulla , ma sento una presenza che si avvicina una presenza' )          
    parola2 = input('inserisci di nuovo:')
    if (parola2=='amici'):
        print ('benvenuti a moria')
    elif    (parola2!= 'amici'):
        print(' Non succede nulla, ma la presenza è molto vicina')
        parola3 = input('inserisci per la terza volta' )
        if (parola3=='amici'):
            print ('benvenuti a moria')
        elif    (parola3!= 'amici'):
            print(' Il mostro è qui , dobbiamo fuggire')
                      




    