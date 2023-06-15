numeroUno = int(input("inserire il primo numero: "))
numeroDue = int(input("inserire il secondo numero: "))
numeroTre = int(input("inserire il terzo numero: "))

minimo = 0
massimo = 0
if (numeroUno > numeroDue and numeroUno > numeroTre):
    massimo = numeroUno
elif (numeroDue > numeroUno and numeroDue > numeroTre):
    massimo = numeroDue
elif (numeroTre > numeroUno and numeroTre > numeroDue):
    massimo = numeroTre
if (numeroUno < numeroDue and numeroUno < numeroTre):
    minimo = numeroUno
elif (numeroDue < numeroUno and numeroDue < numeroTre):
    minimo = numeroDue
elif (numeroTre < numeroUno and numeroTre < numeroDue):
    minimo = numeroTre

print ("il numero minimo è:", minimo, "il numero massimo è:", massimo)
