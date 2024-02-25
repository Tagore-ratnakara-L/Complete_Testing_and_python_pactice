str = "RahulShettyAcadamy.com"
str1= "Ratnakar"
str2= "Acadamy.com"
print(str[0]) #R

print(str[0:5])#Rahul used to print substrings

print(str1+str2) #RatnakarAcadamy.com string concatination

print(str2 in str) #True Substring check
print(str1 in str) #False

print(str.split(".")) # ['RahulShettyAcadamy', 'com'] string separation in python using split
var = str.split(".")
print(f"{var[0]}\n{var[1]}")

# adjusting gaps using strip function
str3= " Ratnakar "
print(str3.strip())
print(str3.lstrip())
print(str3.rstrip())
#o?p as below :-
# Ratnakar
# Ratnakar
#  Ratnakar





