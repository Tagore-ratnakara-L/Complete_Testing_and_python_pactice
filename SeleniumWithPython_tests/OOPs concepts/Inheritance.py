# INHERITANCE
#Concept here is procuring data from parent class .
# methods will automatically called from parent class

from OOPs_demo import Calculator

# class Childimpl(Calculator):
#     num2 = 100
#
#     def getcompletedata(self):
#         return self.number1+self.number2+self.additon()+self.num2
#
# object = Childimpl()
# object.getdata()
# print(object.getcompletedata()) #Calculator.__init__() missing 2 required positional arguments: 'a' and 'b'

#Now import the constructer from parent and assign values in it .
class Childimpl(Calculator):
    num2 = 100

    def __init__(self):
        Calculator.__init__(self,2,10)
    def getcompletedata(self):
        return self.number1+self.number2+self.additon()+self.num2

object = Childimpl()
object.getdata()
print(object.getcompletedata())
#output :-
#I am automatically called when object is created
# i am now executing a method in a class
# 124