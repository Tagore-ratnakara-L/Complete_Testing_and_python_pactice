# for loops fixed iteration
values = [2, 3, 5, 7, 9]
l = []
for i in range(len(values)):
    if values[i] % 2 == 1:
        print(values[i])  # 3,5,7,9
        l.append(values[i])  # Updating list of elements in l
print(l)
print("****************************")

# print sum of frist 5 natural numbers
j = 0
for i in range(1, 6):
    j += i
print(j)
print("****************************")

# print odd numbers < 10
sum = 0
for k in range(1, 10, 2):  # for (i=1;i<10;i+2)
    print(k)  # to print odd numbers below 10
print("****************************")
n = 3
for i in range(n):
    for j in range(i+1):
        print("*",end=" ")
    print("\n")
print("****************************")
# While loop based on condition enters loop and runs untill fals
it = 5
while it >= 1:
    print(it)
    it = it - 1
print("****************************")
# using break key word
it = 5
while it>1:
    if it == 3:
        break
    print(it)
    it -=1
print('while loop execution is done')
print("****************************")

#using continue key word
it = 10
while it>1:
    if it == 9:
        it -=1
        continue
    if it == 3:
        break
    print(it)
    it -=1
print('while loop execution is done')
print("****************************")
