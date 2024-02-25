#what is classes ? it is user defined blueprint or prototype .
# Ex:- Class called calculator then methods are - sum,multiplication,division,substraction
# terminologies in classes - methods , class variables,instance variables , constructures, etc...
#objects for your classes

class Calculator:
    num = 100 # class variable
    #method has created
    # create constructor init as method
    def __init__(self,a,b):
        self.number1 = a #loading values into class instance variables
        self.number2 = b
        print("I am automatically called when object is created")
    def getdata(self):
        print("i am now executing a method in a class")
    def additon(self):
        return self.number1+self.number2
    def substraction(self):
        return self.number1-self.number2
    def multiplication(self):
        return self.number1*self.number2
    def division(self):
        return self.number2/self.number1
#outside of the class create a object and assign class
# obj = Calculator(4,3) # this is enough to call constructor om class
# #I am automatically called when object is created
# obj.getdata()#call method inside the class
#O/P = i am now executing a method in a class
# print(obj.num) # 100
# print(obj.additon())
# print(obj.substraction())
# print(obj.multiplication())
# print(obj.division())
#
# obj1 = Calculator(5,4)
# print(obj1.additon())
# print(obj1.substraction())
# print(obj.multiplication())
# print(obj.division())

