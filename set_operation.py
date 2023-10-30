#set
#implicit
a={'a','b','c','d'}
print(a)
print(type(a))

#explicit
a=set({'a','b','c','d'})
print(a)
print(type(a))

#data type/variable annotation
a:set={'a','b','c','d'}
print(a)
print(type(a))

#add
a={'a','b','c','d'}
a.add('e')
print(a)

#update
#insert
a={'a','b','c','d'}
b={'1','2','3','4'}
a.update(b)
print(a)

#delete
#remove
a={'a','b','c','d'}
a.remove('c')
print(a)

#pop
a={'a','b','c','d','e'}
a.pop()
print(a)

#another functions
#union
a={'a','b','c','d'}
b={'1','2','3','4'}
print(a.union(b))


#intersection
a={'a','b','c','d'}
b={'b','a','g','h'}
print(a.intersection(b))

#disjoint
a={'a','b','c','d'}
b={'1','2','3','4'}
print(a.isdisjoint(b))

#difference
a={'a','b','c','d'}
b={'c','d','e','f'}
print(a.difference(b))

a={'c','d','e','f'}
b={'a','b','c','d'}
print(a.difference(b))

#symmetric difference
a={'a','b','c','d'}
b={'c','d','e','f'}
print(a.symmetric_difference(b))

#symmetric difference update
a={'a','b','c','d'}
b={'c','d','e','f'}
a.symmetric_difference_update(b)
print(a)
print(b)

#issubset
a={'a','b','c','d'}
b={'c','d','e','f'}
print(a.issubset(b))

a={'a','b','c','d'}
b={'a','b','c','d','g','h'}
print(a.issubset(b))


#issuperset
a={'a','b','c','d'}
b={'c','d','e','f'}
print(a.issuperset(b))

a={'a','b','c','d','g','h'}
b={'a','b','c','d'}
print(a.issuperset(b))