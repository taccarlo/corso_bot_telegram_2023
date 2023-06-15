nome = "giovanna"

if nome in names:
    print(nome, "è presente!")

for var in names:
    if var == nome:
        print(nome)
        break
        if var != nome:#non verrà mai eseguita siccome abbiamo bloccato il ciclo
        print("diverso !")


for var in names:
    if var == nome:
        print(nome)
        continue
        if var != nome:#non verrà mai eseguita siccome siamo passati al comando successivo
        print("diverso !")
        

for x in range(3,8,2):
    print(x) 

while count < 5:

list = [655,253,975,262,745,463,208,421,333,987]


print("numeri minori di 470")
for x in list:
    if (x<470):
        print(x