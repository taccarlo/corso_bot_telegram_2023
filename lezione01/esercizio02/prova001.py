print("hello world")

a=int(input("inserire a:"))
b=int(input("inserire b:"))

if(a%2==0)and(b%2==0):
    print("entrabi pari")

if(a%2!=0)and(b%2!=0):
    print("entrabi dispari")

if(a%2!=0)and(b%2==0):
    print("a dispari, b pari")

if(a%2==0)and(b%2!=0):
    print("a pari, b dispari")

    
