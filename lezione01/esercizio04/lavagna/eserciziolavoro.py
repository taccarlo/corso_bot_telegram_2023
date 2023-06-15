

i = 1
while i <= 20:
    print("anno di lavoro", i)
    i += 1

infortunio_debilitante = input("Hai ricevuto un infortunio debilitante? (si/no) ")
if infortunio_debilitante.lower() == "si":
    print("Hai diritto alla pensione!")
else:
    print("Ti mancano 10 anni alla pensione.")