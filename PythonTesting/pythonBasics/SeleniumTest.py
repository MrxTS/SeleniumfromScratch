values = [1, 2, "Stefan", 4, 5]
# List is a data type that allows multiple values and can be different data types

print(values[0])  # 1

print(values[3])  # 4

print(values[-1])  # 5 <-- minus 1 refers to last index in the list

print(values[1:3])  # 2 Stefan

values.insert(3, "Nguyen")
print(values)
values.append("End")
print(values)

values[2] = "STEFAN"
print(values)
del values [0]
print(values)