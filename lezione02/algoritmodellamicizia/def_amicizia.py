def blu():
    r=input("E di bere qualcosa di caldo?(S/N) ")
    if r == ("N"):
        verde()
    else:
        c = input("Scegli: ")
        if c == ("Tè"):
            print("Fatevi 'sto tè")
        elif c == ("Caffè"):
            print("Fatevi 'sto caffè")
        elif c == ("Cicciolata"):
            print("fatevi 'sta cioccolata")
        print("SIETE DIVENTATTI AMICI")
def rossa():
    d=input("Componi il numero di telefono della persona: ")
    r=input("La persona è a casa? (S/N) ")
    if r ==("n") or r==("N") :
        print("Lascio un messaggio, aspetto di essere richiamato")
    else:
       d1= input("ti va di mangiare qualcosa assieme?(S/N) ")
       if d1==("N") or d1==("n"):
           blu()
       else:
            print("Mangiate qualcosa assieme")
            print("Ora siete diventati amici!!")
            
print(rossa())
        
        