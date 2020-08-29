import pyfiglet

result = pyfiglet.figlet_format("D I M A", font="3-d")
print(result)



import codecs

myString = "\a"
print(codecs.escape_decode(bytes(myString, "utf-8"))[0].decode("utf-8"))
myString = "\b"
print(codecs.escape_decode(bytes(myString, "utf-8"))[0].decode("utf-8"))
myString = "\n"
print(codecs.escape_decode(bytes(myString, "utf-8"))[0].decode("utf-8"))
myString = "\t"
print(codecs.escape_decode(bytes(myString, "utf-8"))[0].decode("utf-8"))
myString = "\"\""
print(codecs.escape_decode(bytes(myString, "utf-8"))[0].decode("utf-8"))
myString = "\""
print(codecs.escape_decode(bytes(myString, "utf-8"))[0].decode("utf-8"))
myString = "\'"
print(codecs.escape_decode(bytes(myString, "utf-8"))[0].decode("utf-8"))



x = 10
y = 2
a = x + y
z = x / y
n = x % y
m = x ^ y
print(x, y, a, z, n, m)

