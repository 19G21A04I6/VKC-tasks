
#class
#class method
class math:
    def __init__(self):
        pass
    @classmethod
    def add(cls, a:int,b:int,c:int=0):
        print(a+b+c)
abb=math()
abb.add(3,5,7)
abb=math()
abb.add(6,8,9)

#static method
class math:
    def __init__(self):
        pass
    @staticmethod
    def add( a:int,b:int,c:int=0):
        print(a+b+c)
math.add(4,6,7)



#class variable
class abc:
    def __init__(self):
        pass
    def add(self,a=12):
        print(a)
m=abc()
m.add()

m=abc()
m.add(43)

m=abc()
print(m.add())

#static variable
class asd():
    a:int=10
    def add(self,):
        return self.a
m=asd()
m.a=34
print(m.add())

m=asd()
m.a=78
print(m.add())

m=asd()
print(m.add())
