a = int(input("enter the number :"))
if a < 2:
    print("number is not prime")
else:
    prime=True
    for i in range(2,int(a*0.5)+1):
        if a%2==0:
            prime=False
if prime:
    print("number is  the prime ")
else:
    print("number is not prime")
