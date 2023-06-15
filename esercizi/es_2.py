#Creare due liste denominate x_list e y_list, che contengano rispettivamente 10 istanze delle variabili x e y.
#Creare una lista chiamata big_list, che contiene le variabili x e y, 10 volte ciascuna, concatenando le due liste precedenti.

x = object()
y = object()

# TODO: change this code
x_list = [x]
y_list = [y]
big_list = []

print("x_list contains %d objects" % len(x_list))
print("y_list contains %d objects" % len(y_list))
print("big_list contains %d objects" % len(big_list))

# testing code
if x_list.count(x) == 10 and y_list.count(y) == 10:
    print("Almost there...")
if big_list.count(x) == 10 and big_list.count(y) == 10:
    print("Great!")
