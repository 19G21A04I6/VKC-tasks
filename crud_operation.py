#append
a=["dhahul","sai","jayanth"]
a.append("mohan")
print(a)

#insert
a=["dhahul","sai","jayanth"]
a.insert(1,"mohan sai")
print(a)

#index
a=["dhahul","sai","jayanth"]
print(a.index("sai"))

#count
a=["dhahul","sai","jayanth","sai"]
print(a.count("sai"))

#extend
a=["dhahul","sai","jayanth"]
a1=["Shaik","mohan"]
a.extend(a1)
print(a)

#pop
a=["dhahul","sai","jayanth"]
a.pop(2)
print(a)

#remove
a=["dhahul","sai","jayanth"]
a.remove("sai")
print(a)

#clear
a=["dhahul","sai","jayanth"]
a.clear()
print(a)

#update

#sort
a=[1,3,5,2,4]
a.sort()
print(a)

#reverse
a=["dhahul","sai","jayanth"]
a.reverse()
print(a)