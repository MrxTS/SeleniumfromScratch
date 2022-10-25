file = open('Test.txt')
# read all the contents of file
# print(file.read(5))

# print(file.readline())
# print(file.readline())


# line = file.readline()
# while line != "":
    # print(line)
    # line = file.readline()


# values = [abc, bear, caterpillar, deer, elephant]

for line in file.readlines():
    print(line)


file.close()