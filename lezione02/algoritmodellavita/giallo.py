def giallo():
    print("la persona segue le elementari e le medie ")
    n_bocciature=0
    anno_superiori=0
    print("seguo il " ,anno_superiori, "anno delle superiori")
    anno_superiori=anno_superiori+1
    a=input("sei bocciato?")
    if (a=="si"):
            n_bocciature=n_bocciature+1
            while (n_bocciature>3):
                print("seguo il " +anno_superiori+ "anno delle superiori")
                anno_superiori=anno_superiori+1
                a=input("sei bocciato?")
                if (a=="no"):
                    if anno_superiori==5:
                         print("qualcosa")
                    #parte viola
    else:
        if anno_superiori==5:
            #parte viola
            print("qualcosa")
        else:
             while (n_bocciature>3):
                print("seguo il " +anno_superiori+ "anno delle superiori")
                anno_superiori=anno_superiori+1
                a=input("sei bocciato?")
                if (a=="no"):
                    if anno_superiori==5:
                         print("qualcosa")
                    #parte viola





print("la persona è nata")
giallo()