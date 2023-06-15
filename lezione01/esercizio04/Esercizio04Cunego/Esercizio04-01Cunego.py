#Esercizio04/1
#Prendere in input una lista da tastiera e ritornare una
#lista che scambi le occorrenze di una lettera con un'altra.
def swap_chars(lst, char1, char2):
    swapped_lst = []
    for string in lst:
        swapped_string = string.replace(char1, "_").replace(char2, char1).replace("_", char2)
        swapped_lst.append(swapped_string)
    return swapped_lst

input_lst = input("Inserisci una lista di stringhe: ").split()
char1 = input("Inserisci il primo carattere: ")
char2 = input("Inserisci il secondo carattere: ")
output_lst = swap_chars(input_lst, char1, char2)
print(output_lst)