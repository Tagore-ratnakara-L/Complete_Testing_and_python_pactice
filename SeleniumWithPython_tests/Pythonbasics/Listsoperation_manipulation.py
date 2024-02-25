values = [1,2,"ratna",4,5]

print(values[0]) #1
print(values[1]) #2
print(values[-1]) #5
print(values[1:3]) #using sub index [2, 'ratna']
values.insert(3,"ram")
print(values) #[1, 2, 'ratna', 'ram', 4, 5]
values.append("End")
print(values) #[1, 2, 'ratna', 'ram', 4, 5, 'End']

values[2] = "rahim" #updating
print(values) #[1, 2, 'rahim', 'ram', 4, 5, 'End']
del values[0] # deleting index '0' value
print(values) #[2, 'rahim', 'ram', 4, 5, 'End']

#comparing list with other similar data type
# Tuple is immutable data type it cannot be re assigned elements or interchangable
val = (1,2,"ratna",4,5)

print(val[1]) #2

#Dictionaries practice
dic = {"ram":1,"Ratna":2,3:"rahim"}
# key should wrote left and element is on right assigned
# ratna is key and 2 is its value stored
print(dic["Ratna"]) # 2
print(dic[3]) # rahim
dic["Ratna"] = 5 #updating Ratna key element from 3 to 5
print(dic) #{'ram': 1, 'Ratna': 5, 3: 'rahim'}
dic["rehman"]= 7
print(dic)

n= 3
keys = [1,2,3]
demo = {1: 'Nik', 2:'Kate', 3:'Jane'}
values = [32, 31, 30]
# for i in range(len(keys)):
    #print(demo[i])
dict = {}
for i in range (n):
    #keys[i-1]= demo[i]
    # print(keys[i])
    dict[keys[i]] = [values[i]]
print(dict)