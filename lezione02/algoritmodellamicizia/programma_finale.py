#algoritmo dell'amicizia big bang theory
def algoritmo_rosso():

    NumeroTelefono=print ("Componi il numero di telefono della persona desiderata:\n")



    Risposta1=input ("Sei in casa? S o N.\n")



    if (Risposta1=="S"):
        Risposta2=input ("Ti va di mangiare qualcosa? S o N\n")
        return ("S")

    if(Risposta2=="S"):
        print("Dopo aver mangiato qualcosa insieme sarete diventati amici!\n")
        return ("N")
    else:
        print("manda un messaggio")
        return "N"






def algoritmo_blu(risposta1):
    if risposta1 == "S":
        return "S"
    else: 
        print("ti piace qualcosa ti caldo\n")
        risposta2  = input("ascolta la risposta\n")
        if (risposta2 =="S"):

            scelta = {"te":"fatevi sto te","caffe":"fatevi sto caffe", "cioccolata":"fatevi sta cioccolata\n"}
            scelto = input("scegli\n")
            print(scelta[scelto])
            print("siete diventati amici\n")
            return("S")
        elif risposta2 == "N":
            return "N"
def minifu(n):
    question = input("è qualcosa che voglio fare\n")
    if question == "S":
        print("beh facciamolo dai, siamo amici gegegegega\n")
        return 0
    elif n<=6:
        n+=1
        minifu(n)
    else:
        print("scegli la meno disumana, amici amici e via\n")
        return 0
    
def algoritmo_verde(risposta3):
    n=0
 
    if risposta3 =="S":
        print("siamo amici yesss\n")
    
    else :
 
        minifu(n)
    




algoritmo_rosso()
algoritmo_blu(algoritmo_rosso)
algoritmo_verde(algoritmo_blu)