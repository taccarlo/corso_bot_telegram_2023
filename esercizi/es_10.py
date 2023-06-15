#Scrivi una funzione vendi_libri(), che aiuti nella gestione della vendita di libri in una libreria:
#Controlla se il libro richiesto è presente sugli scaffali della libreria
#Qualora il libro sia presente, ne decrementa il numero di copie (eventualmente rimuovendo il titolo se il numero di copie presenti arriva a 0) e segnala che la vendita ha avuto successo
#Se il libro non è disponibile, viene messo in un elenco di libri da ordinare e viene comunicato che la vendita non ha avuto successo
#La funzione deve restituire valore booleano True o False in base all'esito della vendita.

scaffale = {"Così parló Zarathustra": 10, "Elon Musk - Biografia": 7, "End Of Jobs": 5,
            "L'Alchimista": 1, "I Fratelli Karamazov": 2, "Delitto e Castigo": 1}
ordini = []

def vendi_libri(scaffale, libro):
    #inserire il codice qui


libro_richiesto = input("che libro stai cercando: ")
vendi_libri(scaffale, libro_richiesto)