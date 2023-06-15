#giallo#
#Creazione variabili#
n_bocciature = 0
anno_superiori = 1
b = 0

#creazione funzioni#
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
"""FUNZIONE SUL LAVORO"""
        
#svolgimrnto#
print("La persna è nata")
print("La persona segue elementari e medie")
bocciature()
    
