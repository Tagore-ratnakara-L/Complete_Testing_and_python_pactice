# in python functions is a group of related statements that perform a specific task
# def is identifier used to create a function
# demo_function is name of function defined
# function declaration

def Greeting(name):
    print("Good morning!," + name)


# Function call
Greeting("Ratnakar")
print("**************************************")


def demo_function():
    a = int(input("Enter 1st number:" ))
    b = int(input("Enter 2nd number: "))
    a +=b
    print(a)
#Function call
demo_function()
print("**************************************")
#method-2
def demo_function(a, b):
    a += b
    print(a)

# Function call
demo_function(a=int(input("Enter 1st number:")), b=int(input("Enter 2nd number: ")))
print("**************************************")

#using return to store values in function
def Addinteger(a,b,):
    return a + b

# Function call
print(Addinteger(a=4, b=8))

