#dictionary create methods
#fromkeys
key=('firstname','lastname','mail')
value=""
a=dict.fromkeys(key,value)
print(a)

#setdefault
a:dict=({})
a.setdefault('firstname','dhahul')
a.setdefault('lastname','shaik')
a.setdefault('mail','d@gmail.com')
print(a)


#update
a:dict={'firstname':'dhahul','lastname':'shaik','mail':'d@mail.com'}
a.update({'firstname':'Dhahul'})
print(a)

#delete
#pop
a:dict={'firstname':'dhahul','lastname':'shaik','mail':'d@mail.com'}
a.pop('firstname')
print(a)

#popitem
a:dict={'firstname':'dhahul','lastname':'shaik','mail':'d@mail.com'}
a.popitem()
print(a)

#clear
a:dict={'firstname':'dhahul','lastname':'shaik','mail':'d@mail.com'}
a.clear()
print(a)


#Accessing the dictionary
#accessing with the key
a:dict={'firstname':'dhahul','lastname':'shaik','mail':'d@mail.com'}
print(a['firstname'])

#get
a:dict={'firstname':'dhahul','lastname':'shaik','mail':'d@mail.com'}
print(a.get('firstname'))

a:dict={'firstname':'dhahul','lastname':'shaik','mail':'d@mail.com'}
print(a.get('firstname1'))


#keys
a:dict={'firstname':'dhahul','lastname':'shaik','mail':'d@mail.com'}
print(a.keys())

#values
a:dict={'firstname':'dhahul','lastname':'shaik','mail':'d@mail.com'}
print(a.values())


#items
a:dict={'firstname':'dhahul','lastname':'shaik','mail':'d@mail.com'}
print(a.items())