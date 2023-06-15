#Concatenare due liste prese da tastiera
lista1 = []
lista2 = []

n = int(input('Quanti valori vuoi inserire nelle liste? '))
            
for i in range (n) :
    val= input('Dammi un valore da inserire nella lista 1 ')
    lista1.append(val)
            
for i in range (n):
    val= input('Dammi un valore da inserire nella lista 2 ')
    lista2.append(val)           
            
outputlist = [lista1+lista2]
print('Le due liste unite danno cone lista finale', outputlist)