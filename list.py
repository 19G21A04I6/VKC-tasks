#list reversing
a = ["dhahul","sai","jayanth"]
reverse=a[::-1]
print(reverse)

#slicing
a = ["dhahul","sai","jayanth"]
print(a[0:2])
print(a[0:])
print(a[:2])
print(a[0:3])

#string reverse
a = "Dhahul"
reverse_str=a[::-1]
print(reverse_str)

#reverse list without slicing
a = ["Dhahul","sai","jayanth"]
a.reverse()
print(a)

#length of the list
a = ["Dhahul","sai","jayanth"]
print(len(a))

#reverse string without slicing\
n= "Dhahul"
string_a = " "
for i in n:
    string_a = i + string_a
print(string_a)