# encapsulation = This is the concept of wrapping data and methods 
# that work with data in one unit. 

# Access modifiers:1.Private 2.Public 3.Protected
# Pyhton does not recommend protected modifier

# Private
class Student:
    school="MVM"
    def __init__(self,name,age):
        self.__name=name
        self.__age=age
    def details(self):
        print("Name=",self.__name)
        print("Age=",self.__age)
        print("School=",Student.school)
class Marks(Student):
    def marks(self,hindi,english):
        self.hindi=hindi
        self.english=english
    def complete_details(self):
        print("Name=",self.__name)
        print("Age=",self.__age)
        print("School=",Student.school)
        print("Hindi=",self.hindi)
        print("English=",self.english)
obj=Marks("Vaishu",22)
obj.__name="Maanu bhoyar"
obj.details()
obj.marks(78,87)
Student.school="Maharishi Vidhya Mnadir"
obj.complete_details

