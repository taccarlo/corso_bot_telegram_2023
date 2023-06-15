input("componi numero di telefono del tuo amico: ")

def casa():
    var1 = int(input("è in casa? 0/1 "))

    if (var1==0):
        print("lascia un messaggio e aspetta di essere richiamato")

    if(var1==1):
        print("ti va di mangiare qualcosa insieme? 0/1")

        var2 = int(input("...ascolto riposta... 0/1 "))

        if(var2==0):
            print("evviva! Andiamo!")

        if(var2==1):
            domanda()   
casa()
