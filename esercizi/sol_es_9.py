#Scrivi un programma che trovi tutti i numeri divisibili per 7 ma non multipli di 5,
#tra il 2000 e il 3200 (entrambi inclusi).
#I numeri ottenuti devono essere stampati in una sequenza separata da virgole su un'unica riga.

#Suggerimenti:
#Considera l'uso del metodo range(#begin, #end).
risultato = []
for i in range(2000, 3201):
    if (i%7==0) and (i%5!=0):
        risultato.append(str(i))

print(','.join(risultato))