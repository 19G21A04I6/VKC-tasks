#Append
#operator overloading
a = "Dhahul"
b = "Shaik"
print(a + " " + b)

#insert Full Name
a = "Dhahul"
b = "Shaik"
print("Full name:" ,a + " " + b)


#f'string /interpolation :
a = "Dhahul"
b = "Shaik"
print(f'{a} {b}')

#insert Full Name
a = "Dhahul"
b = "Shaik"
print("Full Name :",f'{a} {b}')

#string join
a = "Dhahul"
b = "Shaik"
l=( a,b )
print(" ".join(l))

#insert Full Name
a = "Dhahul"
b = "Shaik"
n = ("Full Name",a , b)
print(" ".join(n))

#split/sliptlines/partition/rpartition
#split
email = "dhahulshaik938@gmail.com"
print(email.split("@"))


#split lines
a=""" 5-4-92,
agraharapet,
naidupet,
nellore,
Andhra Pradesh"""
print(a.splitlines())

#partition
a ="dhahulshaik@gmail.com"
print(a.partition("a"))


#rpartition
a="dhahulshaik@gmail.com"
print(a.rpartition("a"))

