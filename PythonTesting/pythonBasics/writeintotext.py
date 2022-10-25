# read the file and store all the lines in the list
# reserve the list
# write list back to the file

with open('Test.txt', 'r') as reader:
    content = reader.readlines() # [ape, bear, caterpillar, deer, elephant]
    reversed(content)  # [elephant, deer, caterpillar, bear, ape]
    with open('Test.txt', 'w') as writer:
        for line in reversed(content):
            writer.write(line)