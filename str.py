# string
#implicit
a = "Dhahul"
print(a)
print(type(a))

#explicit
a = str("Dhahul")
print(a)
print(type(a))

#Data type /variable annotation
a: str = "Dhahul"
print(a)
print(type(a))
#binary
a = str(0b1010)
print(a)
print(type(a))
#octal
a = str(0o1234)
print(a)
print(type(a))
#hexa
a = str(0xabc)
print(a)
print(type(a))
#boolean
a = str(True)
print(a)
print(type(a))
#b00lean conversion
a = bool("abc")
print(a)
print(type(a))
#hexa conversion
a = hex("abc")
print(a)
print(type(a))
#octal conversion
a = oct("abc")
print(a)
print(type(a))
#binary conversion
a = bin("abc")
print(a)
print(type(a))