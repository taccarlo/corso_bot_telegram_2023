numeroUno = int(input("inserire il primo numero: "))
numeroDue = int(input("inserire il secondo numero: "))

if (numeroUno %2 == 0):
    print("pari")
else:
    if (numeroDue %2 != 0):
        print ("entrambi dispari")
    else:
        print ("primo dispari, secondo pari")