from calcolatore import ottieniRisposta

numeroMagico = 0

def Stampa():
    print("Il tuo numero è tra i seguenti?")
    i = 0
    list=[]
    for x in range(8, 63):
        if(i<8):
            list.append(x)
            i += 1
        elif(i < 15):
            i += 1
        else:
            i=0
    print(list)
    global numeroMagico
    num = numeroMagico
    numeroMagico = ottieniRisposta(num, 3)

def primo():
    print("Il tuo numero è tra i seguenti?")
    list=[]
    for i in range(2, 62, 4):
        list.append(i)
        list=list+[i+1]
    print(list," ")

    global numeroMagico
    num = numeroMagico
    numeroMagico = ottieniRisposta(num, 1)

def numeriDispari():
    print("Il tuo numero è tra i seguenti?")
    list = []
    for x in range(1, 63,2):
        list.append(x)
    print(list, " ")

    global numeroMagico
    num = numeroMagico
    numeroMagico = ottieniRisposta(num, 0)

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

    global numeroMagico
    num = numeroMagico
    numeroMagico = ottieniRisposta(num, 2)

def bello():
    print("Il tuo numero è tra i seguenti?")
    list = []
    for x in range(16, 32):
        list.append(x)
    for x in range(48, 63):
        list.append(x)
    print(list)
    global numeroMagico
    num = numeroMagico
    numeroMagico = ottieniRisposta(num, 4)

def neuroni():
    print("Il tuo numero è tra i seguenti?")
    list = []
    for x in range(32,63):
        list.append(x)
    print(list)


global numeroMagico
num = numeroMagico
numeroMagico = ottieniRisposta(num, 5)

    
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

print("Il numero pensato è ", numeroMagico)