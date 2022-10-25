print("hello")
# here are the comments I have defined

a = 3
print(a)

Str = "Hello World"
print(Str)

b, c, d = 5, 6.4, "Great"
print(b, c, d)

# print("Value is"+b) <-- does not work like this

print("{} {}".format("Value is", b))

print("{} {} {}".format("This is a datatype", b , c))

print(type(b))
print(type(c))
print(type(d))

# Tuple - Same as LIST Data type but immutable
val = [1, 2, "Stefan", 4.5]

print(val[1])

#val[2] = "STEFAN"

print(val)

dic = {"a": 2, 4: "bcd", "c": "Hello World"}
print(dic[4])
print(dic["c"])
print(dic)