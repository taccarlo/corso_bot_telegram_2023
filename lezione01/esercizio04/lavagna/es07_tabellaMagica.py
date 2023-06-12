count = 0
list1 = []
list2 = []
list3 = []
list4 = []
list5 = []
list6 = []

for x in range (1, 63, 2) :
    list1.append(x)
print (list1)
n1 = input("Il numero è tra i seguenti?")
if n1 == "si" :
    count += 1
    
    
for x in range (2, 63,) :
    if x % 4 <= 1:
        continue
    list2.append(x)
print (list2)
n1 = input("Il numero è tra i seguenti?")
if n1 == "si" :
    count += 2
    
    
for x in range (4, 63, ) :
    if x % 8 <= 3:
        continue
    list3.append(x)
print (list3)
n1 = input("Il numero è tra i seguenti?")
if n1 == "si" :
    count += 4
    
    
for x in range (8, 63) :
    if x % 16 <= 7:
        continue
    list4.append(x)
print (list4)
n1 = input("Il numero è tra i seguenti?")
if n1 == "si" :
    count += 8
    
    
for x in range (16, 63):
    if x % 32 <= 15:
        continue
    list5.append(x)
print (list5) 
n1 = input("Il numero è tra i seguenti?")
if n1 == "si" :
    count += 16
    
    
for x in range (32, 63) :
    list6.append(x)
print (list6)
n1 = input("Il numero è tra i seguenti?")
if n1 == "si" :
    count += 32
    
print ("Il tuo numero è", count)