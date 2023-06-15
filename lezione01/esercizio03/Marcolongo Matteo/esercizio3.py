print('scrivete amici ed entrate')

for x in range(3):
    parola = input('Inserisci una parola: ')
    parola = str(parola)

    if(parola == 'amici'):
        print('Benvenuti a moria')
        break
    elif(parola != 'amici' and x < 2):
        print('Non succede nulla ma sento un presenza molto vicina')
    elif(parola != 'amici' and x == 2):
        print('Il mostro è qui dobbiamo scappare')
