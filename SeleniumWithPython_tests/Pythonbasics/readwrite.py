file = open('text.txt')
#read method used to read all the contents in the file

# print(file.read())
#output
# a
# b
# c
# d
# e
#read n number of characters by passing parameter
#content in the text file
# apple
# ball
# cat
# dog
# eagle
# print(file.read(5)) #apple
#comment above before read line
#readline method is used to read the lines format instead of characters
# print(f"{file.readline()}\n{file.readline()}")
# apple
#
# ball

# file.close()

#print all the content line by line using readline
#method -1
# line = file.readline()
# while line!="":
#     print(line)
#     line = file.readline()
    # #output print as
    # apple
    #
    # ball
    #
    # cat
    #
    # dog
    #
    # eagle
#Method-2
for line in file.readlines():
    print(line)
file.close()
# #output print as
    # apple
    #
    # ball
    #
    # cat
    #
    # dog
    #
    # eagle

