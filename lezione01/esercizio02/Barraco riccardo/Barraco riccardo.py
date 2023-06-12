n=int(input("inserisci un numero"))
m=int(input("inserisci un altro numero"))
if(n%2==0) and (m%2==0):
  print("i numeri sono entrambi pari")
elif(n%2==0) and (m%2!=0):
    print("il primo numero è pari mentre il secondo è dispari")
elif(n%2!=0) and (m%2==0):
    print("il prmo numero è dispari e il secondo è pari")
else:
    print("i numeri sono entrambi dispari")