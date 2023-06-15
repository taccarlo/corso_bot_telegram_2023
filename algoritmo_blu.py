def gruppoblu(risposta1):
    if risposta1 == "S":
        return "S"
    else: 
        print("ti piace qualcosa ti caldo")
        risposta2  = input("ascolta la risposta")
        if (risposta2 =="S"):

            scelta = {"te":"fatevi sto te","caffe":"fatevi sto caffe", "cioccolata":"fatevi sta cioccolata"}
            scelto = input("scegli\n")
            print(scelta[scelto])
            print("siete diventati amici")
            return("S")
        else:
            return "N"

