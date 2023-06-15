def funzione_1():
    print("La persona è nata")
    print("La persona segue le elementari e le medie")
    n_bocciature = 0
    anno_superiori = 1
    while (n_bocciature <= 2) and (anno_superiori <= 5):
        print("Seguo il ", anno_superiori, "anno delle superiori")
        esito = input("Bocciato? ")
        if esito == "si":
            n_bocciature += 1
        elif esito == "no":
            anno_superiori += 1
            
    if n_bocciature == 3 or anno_superiori == 6:
        print("La persona entra nel mondo del lavoro")
        funzione_2()
    
def funzione_2():
    i = 1
    while i <= 20:
        print("anno di lavoro", i)
        i += 1

    infortunio_debilitante = input("Hai ricevuto un infortunio debilitante? (si/no) ")
    if infortunio_debilitante.lower() == "si":
        print("Hai diritto alla pensione!")
    else:
        print("Ti mancano 10 anni alla pensione.")
        funzione_3()
    
    
def funzione_3():    
    promozioni = input("Quante promozioni hai ottenuto negli ultimi anni di lavoro? ")
    if promozioni >="3":
        print("Hai ottenuto una promozione a capo d'azienda")
    if promozioni <"3":
        print("E' il momento di andare in pensione")
funzione_1()