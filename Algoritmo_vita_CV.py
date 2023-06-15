#giallo#
#Creazione variabili#
n_bocciature = 0
anno_superiori = 1
b = 0

#creazione funzioni#
#def anni lacvoro#
def anni_lavoro():
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
#calcolo bocciature
def bocciature():
    global anno_superiori
    global n_bocciature
    global b
    while anno_superiori <= 5 and n_bocciature <3:
        print("Segue l'anno di superiori", anno_superiori)
        b = int(input("Sei stato bocciato? 1=si 0=no  "))
        n_bocciature = n_bocciature + b
        if b == 0:
            anno_superiori = anno_superiori + 1   
    
    print("Lavoro!")
        
        
#svolgimrnto#
print("La persna è nata")
print("La persona segue elementari e medie")
bocciature()
anni_lavoro()
    
