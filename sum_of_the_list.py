n=int(input())
sum=0
while n!=0:
    sum=sum+(n%10)
    n=n//10
print(sum)

n=123
sum=0
for item in str(n):
    sum=sum+int(item)
print(sum)