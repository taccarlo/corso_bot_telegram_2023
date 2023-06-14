#Scrivi una funzione che data in ingresso una lista A contenente n parole, chieda all’utente di inserire una lettera e restituisca in output una lista B di parole che iniziano con la lettera inserita dall’utente.

def first_letter(lista_parole, prima_lettera):
    risultato = []
    for parola in lista_parole:
        if parola.startswith(prima_lettera):
            risultato.append(parola)
    
    return risultato



lista_parole = ["monitor", "muro", "giornale", "computer", "bottiglia"]
prima_lettera = input("inserire lettera: ")

print(first_letter(lista_parole, prima_lettera))
