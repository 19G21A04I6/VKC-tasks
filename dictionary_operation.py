#dictionary
#example
#implicit
a={'firstname ':'Dhahul','second name':'Shaik','gender':'Male','email':'dhahulshaik938@gmail.com'}
print(a)
print(type(a))

#explicit
a=dict({'firstname ':'Dhahul','second name':'Shaik','gender':'Male','email':'dhahulshaik938@gmail.com'})
print(type(a))

#data type / variable annotation
a:dict={'firstname ':'Dhahul','second name':'Shaik','gender':'Male','email':'dhahulshaik938@gmail.com'}
print(type(a))


#set default
a={'firstname ':'Dhahul','second name':'Shaik','gender':'Male','email':'dhahulshaik938@gmail.com'}
a.setdefault('firstname','SHAIK')
print(a)