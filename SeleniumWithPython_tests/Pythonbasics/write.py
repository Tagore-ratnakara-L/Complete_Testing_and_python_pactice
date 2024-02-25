# file = open('write.txt')
#
# file.close()
#above are basic usage but genaral usage single line code is enough as below

# with open('write.txt') as file:
    # this will automatically closes file when it is done

    # specify python as it is read or write as with open('write.txt', 'condition') as file:
    #to read
# with open('write.txt', 'r') as file:
#     # to write
# with open('write.txt', 'w') as file:

# read the list
with open('write.txt', 'r') as reader:
    content = reader.readlines() #['apple\n', 'ball\n', 'cat\n', 'dog\n', 'eagle\n', 'fox\n', 'goat']
    reversed(content)
    with open('write.txt','w') as writer:
        for line in reversed(content):
            writer.write(line)