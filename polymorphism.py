#overloading method
class data:
    def __add__(self, a:int,b:int):
        print(a+b)
    def __add__(self,a:int,b:int,c:int=0):
        print(a+b+c)
    def __ddd__(self,a:str,b:str,c:str=0):
        print(a+" "+b+" "+c)
    def __ele__(self,a:str,b:str):
        print(a+" "+b)
cal=data()
cal.__add__(2,4)
cal.__add__(4,6,7)
cal.__ddd__("shaik","dhahul","23y")
cal.__ele__("Ben","10")

#overriding method
class employee():
    __data__=int(input("Enter the employee montly salary = "))
    def sal(self)->float:
        return self.__data__*12
class contract_employee():
    __hours__=int(input("Enter the contractor employee working hours = "))
    __income__=500
    def sla(self)->float:
        return self.__hours__*500
emp=employee()
emp1=contract_employee()
print("Yearly salary for employee =",emp.sal())
print("Today salary for contractor employee = ",emp1.sla())
