# Inheritance and Advanced OOP Features

# base class

class Animal:
    def show1(self):
        print("Animals make different sounds. ")
        
# derived class

class Dog(Animal):
    def show2(self):
        print("Dog barks! ")

# Animals make different sounds. # From Animal class
output1=Animal()
output1.show1()        
 
#from dog class       
output2=Dog()
#output2.show1()
output2.show2()