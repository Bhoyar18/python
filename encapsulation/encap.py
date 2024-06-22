# encapsulation = This is the concept of wrapping data and methods 
# that work in one unit. 

# Access modifiers:1.Private 2.Public 3.Protected
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




# Constructor
class Faculty:
    def __init__(self,a,b,c):
        self.id=a
        self.name=b
        self.age=c
    def display(self):
        print("Faculty id :",self.id)
        print("Faculty name :",self.name)
        print("Faculty age :",self.age)
a=Faculty(1,"Vaishu",22)
a.display()        