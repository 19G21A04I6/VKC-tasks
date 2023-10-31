
# fibonacci series
def fib():
    n = 10
    n1 = 0
    n2 = 1
    i = 1
    if n == 1:
        print(n1)
    elif n == 2:
        print(n2)
    else:
        print(n1, n2, end="")
        while i < n - 1:
            n3 = n1 + n2
            print(n3, end="")
            n1 = n2
            n2 = n3
            i = i + 1
fib()

#parameterless/non-returnable/general function :
def add():
    a=10
    b=20
    print(a+b)
add()

#parameterized function :
def add(a,b):
    print(a+b)
add(10,30)

#function with named parameters :
def add(internal1,internal2):
    print(internal1+internal2)
add(10,20)

def add(internal1,internal2):
    a=10
    b=20
    print(internal1+internal2)
add(internal2=a,internal1=b)

#substraction
