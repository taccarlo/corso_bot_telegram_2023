def pensione():
    print ("Ultimi anni di lavoro.")
    dod = int(input("Quante promozioni? "))
    if dod <= 3:
        print("Pensione")
    if dod > 3:
        print ("Capo azienda")
        print("Pensione")
    else:
        pensione()