#Scrivi una funzione che data in ingresso una lista A contenente n parole, restituisca in output una lista B di interi che rappresentano la lunghezza delle parole contenute in A.

def char_counter(lista_a):
    lista_b = []
    for parola in lista_a:
        lista_b.append(len(parola))
    return lista_b


lista_parole = ["monitor", "muro", "giornale", "computer", "bottiglia"]
print(char_counter(lista_parole))