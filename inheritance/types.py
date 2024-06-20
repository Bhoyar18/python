
# Types of Inheritance
# SINGLE INHERITANCE = Single Inheritance is the simplest form of 
# inheritance where a single child class is derived from a single parent class

class Parent:                  
    # parent class
    def hello1(self):
        print("This is Parrent Class")
class Child(Parent):    
  # child class
    def hello2(self):               
        print("This is Child Class")                            
a = Child()                 
a.hello1()                 
a.hello2()         