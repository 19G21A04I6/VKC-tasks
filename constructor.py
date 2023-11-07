#constructor
#default constructor
class employee_name:
    def full_name(self,firstname,lastname):
        print(firstname+" "+lastname)
emp=employee_name()
emp.full_name("Dhahul","Shaik")


#parameter less constructor
class employee:
    def __init__(self):
        pass
    def full_name(self,firstname,lastname):
        print(firstname+" "+lastname)
emp1=employee
emp.full_name("Dhahul","Shaik")


#parameteraized constructor

class employee_2:
    __fname__:str=" "
    __lname__:str=" "
    def __init__(self,fname,lname):
        self.__fname__=fname
        self.__lname__=lname
    def full_name(self):
        print(self.__fname__+" "+self.__lname__)
emp2=employee_2("Dhahul","Shaik")
emp2.full_name()


