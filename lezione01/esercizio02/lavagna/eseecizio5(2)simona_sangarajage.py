'''Leggere un numero da terminale e controllare se è pari;
se lo è stampate “pari” a terminale, altrimenti leggete un secondo numero.
Se il secondo numero è dispari stampate “entrambi dispari”, 
altrimenti stampate “primo dispari, secondo pari'''


numero1 =int(input('inserisci un numero'))
if (numero1%2)==0:
    print ('pari')

else:
    numero2 = int(input('inserisci un\'altro numero'))
    if (numero2%2==1):
        print('entrambi dispari')
    else:
         (numero1%2==0) and (numero2%2==1)
         print ('primo dispari e secondo pari')
