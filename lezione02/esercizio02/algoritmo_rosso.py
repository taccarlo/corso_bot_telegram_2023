#algoritmo dell'amicizia big bang theory
def grupporosso():

    NumeroTelefono=print ("Componi il numero di telefono della persona desiderata:")

    NumeroTelefono=int(NumeroTelefono) 

    Risposta1=print ("Sei in casa? S o N.")



    if (Risposta1=="S"):
        Risposta2=print ("Ti va di mangiare qualcosa? S o N")
        return ("S")

    if(Risposta2=="S"):
        print("Dopo aver mangiato qualcosa insieme sarete diventati amici!")
        return ("N")
