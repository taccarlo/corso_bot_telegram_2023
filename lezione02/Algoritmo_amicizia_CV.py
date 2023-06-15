

































def anni_lavoro()
    print("lavoro")
    c = 2000
    for i in range(0,19):
        c = c+1
        print("anno di lavoro", c)
    
    z = input("INFORTUNIO DEBILITANTE ?")
    if z == "vero" or z == "Vero":
        print("pensione")
    else:
        print("ultimi anni di lavoro")
        w = input("quante promozioni")
        if w >= "3":
            print("capo d'azienda"),print("pensione")
        else:
            print("pensione") 
