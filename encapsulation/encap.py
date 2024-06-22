# encapsulation = This is the concept of wrapping data and methods 
# that work in one unit. 
# In Python, encapsulation is achieved by using access modifiers to 
# control the visibility of class attributes and methods.

# Access modifiers are keywords that determine the visibility of 
# class members, which include attributes and methods. There are three 
# access modifiers in Python: public, protected, and private.
# 1.Private 2.Public 3.Protected
# Pyhton does not recommend protected modifier

# Private:In the case of private access modifiers, the variables and 
# functions can only be accessed within the class. The private restriction 
# level is the highest for any class. To declare the data members as 
# private, we use a double underscore “_­_” sign before the data members 
# of the class. 
# class Student:
#     school="MVM"
#     def __init__(self,name,age):
#         self.__name=name
#         self.__age=age
#     def details(self):
#         print("Name=",self.__name)
#         print("Age=",self.__age)
#         print("School=",Student.school)
# class Marks(Student):
#     def marks(self,hindi,english):
#         self.hindi=hindi
#         self.english=english
#     def complete_details(self):
#         print("Name=",self.__name)
#         print("Age=",self.__age)
#         print("School=",Student.school)
#         print("Hindi=",self.hindi)
#         print("English=",self.english)
# obj=Marks("Vaishu",22)
# obj.__name="Maanu bhoyar"
# obj.details()
# obj.marks(78,87)
# Student.school="Maharishi Vidhya Mnadir"
# obj.complete_details

# Public:Public members are accessible from anywhere, 
# both inside and outside the class.

class Person:
    # constructor
    def __init__(self, name, age):
        # public data members
        self.personName = name
        self.personAge = age
    # public member function
    def displayAge(self):
        # accessing public data member
        print("Age of the person is : ", self.personAge )
# creating object of the class
obj = Person("Vaishu", 22)
# accessing public data member
print("Name of the person is : ", obj.personName)
# calling public member function of the class
obj.displayAge() 

# Constructor
# class Faculty:
#     def __init__(self,a,b,c):
#         self.id=a
#         self.name=b
#         self.age=c
#     def display(self):
#         print("Faculty id :",self.id)
#         print("Faculty name :",self.name)
#         print("Faculty age :",self.age)
# a=Faculty(1,"Vaishu",22)
# a.display()        