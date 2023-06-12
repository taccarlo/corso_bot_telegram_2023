numero = int(input("inserire un numero compreso tra 1 e 5"))

if (numero >= 1 and numero <=5):
    if (numero == 2 or numero == 3 or numero == 5):
        print ("il numero", numero, "è un numero primo")
    else:
        print ("il numero", numero, "non è un numero primo")
else:
    print ("il numero non è compreso tra 1 e 5")