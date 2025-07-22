# Introduction to OOP Concepts

#class

class Person():
    
    def __init__(self,name,age): #constructor
        self.name=name
        self.age=age
    
    def show(self): #method
        print(f"Name:{self.name},Age:{self.age}")

info=Person("Alice",25)
info.show()    