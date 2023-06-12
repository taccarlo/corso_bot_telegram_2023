


# Prendere in input una lista da tastiera e scambiare le occorrenze di una lettera con un'altra
def scambia_lettere(lista, a, b):
    nuova_lista = []
    for elemento in lista:
        if elemento == a:
            nuova_lista.append(b)
        elif elemento == b:
            nuova_lista.append(a)
        else:
            nuova_lista.append(elemento)
    return nuova_lista

# Concatenare due liste prese da tastiera
lista1 = input("Inserisci la prima lista: ").split()
lista2 = input("Inserisci la seconda lista: ").split()
lista_concatenata = lista1 + lista2

# Testare la funzione di scambio lettere
lista_da_scambiare = input("Inserisci la lista da scambiare: ").split()
lettera1 = input("Inserisci la prima lettera da scambiare: ")
lettera2 = input("Inserisci la seconda lettera da scambiare: ")
lista_scambiata = scambia_lettere(lista_da_scambiare, lettera1, lettera2)

# Stampare i risultati
print("Lista concatenata:", lista_concatenata)
print("Lista scambiata:", lista_scambiata)
