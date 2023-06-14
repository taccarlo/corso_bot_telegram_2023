#Aggiungere numeri e stringhe agli elenchi corretti usando il metodo "append" list. 
#Devi aggiungere i numeri 1, 2 e 3 all'elenco "numbers" e le parole "ciao" e "mondo" alla variabile strings.
#Compilare la variabile second_name con il secondo nome nell'elenco dei nomi, utilizzando l'operatore parentesi [].  

numbers = []
strings = []
names = ["John", "Eric", "Jessica"]

# write your code here
second_name = None

numbers.append(1)
numbers.append(2)
numbers.append(3)

strings.append("ciao")
strings.append("mondo")

second_name = names[1]

# this code should write out the filled arrays and the second name in the names list (Eric).
print(numbers)
print(strings)
print("The second name on the names list is %s" % second_name)
