from PRIMI import primo
from gruppoGIULIA import Stampa

def numeriDispari():
    print("Il tuo numero è tra i seguenti?")
    list = []
    for x in range(1, 63,2):
        list.append(x)
    print(list, " ")

def secondo():
    i=4
    listsecondo=[]
    print("Il tuo numero è tra i seguenti?")
    while i<63:
        for j in range(4):
            listsecondo=listsecondo+[i]
            i=i+1
        i=i+4
    print(listsecondo)

def bello():
    print("Il tuo numero è tra i seguenti?")
    list = []
    for x in range(16, 32):
        list.append(x)
    for x in range(48, 63):
        list.append(x)
    print(list)

def neuroni():
    print("Il tuo numero è tra i seguenti?")
    list = []

    for x in range(32,63):
        list.append(x)
    print(list)


    
# prima domanda (1,3,5)
numeriDispari()
# seconda domanda (partendo da 2 scrivo 2 numeri sì e 2 no) PRIMO
primo()
# terza domanda (partendo da 4 scrivo 4 numeri sì e 4 no) SECONDO
secondo()
# quarta domanda (partendo da 8 scrivo 8 numeri sì e 8 no) GIULIA
Stampa()
# quinta domanda (partendo da 16 scrivo 16 numeri sì e 16 no) BELLO
bello()
# sesta domanda (partendo da 32 scrivo 32 numeri sì e 32 no) TRE NEURONI SOMMATI
neuroni()