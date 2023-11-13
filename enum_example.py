from enum import Enum
class student(Enum):
    Dhahul=1
    Mohansai=2
    Ahmed=3
    Naveen=4
    Rajeev=5
    Preetam=6
    Sundar=7
#check student are regular or not
def checkdata(value)->str:
    result:str=""
    match(value):
        case student.Dhahul.value:
            result="Regular"
        case student.Mohansai.value:
            result = "Regular"
        case student.Ahmed.value:
            result = "Regular"
        case student.Naveen.value:
            result = "Regular"
        case student.Rajeev.value:
            result = "Regular"
        case student.Preetam.value:
            result = "Irregular"
        case student.Sundar.value:
            result = "Irregular"
    return result
dtu=int(input("Enter the student data :1.Dhahul,2.Mohansai,3.Ahmed,4.Naveen,5.Rajeev,6.Preetam,7.sundar: "))
print(checkdata(dtu))


#Exception handling
try:
    a=int(input("Enter a value :"))
    b=int(input("Enter a value :"))
    print(a%b)
except:
    print("exception occur")
else:
    print("program executed successfully ")
finally:
    print("program completed")


