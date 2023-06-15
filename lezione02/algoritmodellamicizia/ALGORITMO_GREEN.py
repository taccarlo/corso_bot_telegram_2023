def algoritmo_verde(risposta3):
    
    
    if risposta3 == "N":

        print("Svaghiamoci un pò... ", "Cos'altro ti va di fare?")
        question = print("E' una cosa che piace anche a me?")
    
    if question == "S":
        print("Dopo esservi svagati insieme, diventerete amici")
        return("N")
    
    if question == "N":
        n += 1
        
        if n > 6:
            print("Scegli tra tutte le opzioni che ti sembri meno disumana, fattela piacera, svagati un po' e diventerete amici")
            return("S")
        else:
            print(question)
            return("N")