n = 0
def verde():
    if n == 0:
        print("Allora sgranchiamoci un po'...")
    voglia = input("... Cos'altro ti va di fare? ")
    risposta = input("É una cosa che mi va di fare?(S/N) ")
    if risposta == "s" or risposta == "S":
        print ("E facciammolo insieme dai...")
        print ("Svagetevi un po' insieme ")
        print ("Siete diventati amici")
    if risposta == "n" or risposta == "N":
       No()
def No():
    global n
    n = n + 1
    if n < 7:
        verde()
    else:
        print ("Scegli tra le opzioni quelle che ti appare meno disumana")
        print ("Fattela piacere")
        print ("Svagetevi un po' insieme ")
        print ("Siete diventati amici")
        
def blu():
    r=input("E di bere qualcosa di caldo?(S/N) ")
    if r == ("N") or r == ("n"):
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
        d1= input("ti va di mangiare qualcosa assieme?(S/N) ")
        if d1==("N") or d1==("n"):
            blu()
    else:
       d1= input("ti va di mangiare qualcosa assieme?(S/N) ")
       if d1==("N") or d1==("n"):
           blu()
       else:
            print("Mangiate qualcosa assieme")
            print("Ora siete diventati amici!!")
            
rossa()
        
        