lista = ["p","i","p","p","o"]
i = 0
n1 = input ("Inserire il carattere da sostituire ")
n2 = input ("Inserire il carattere con cui sostituirlo ")

while i < 5:
    if (lista[i] == n1) :
        lista [i] = n2
    i = i + 1
print (lista)