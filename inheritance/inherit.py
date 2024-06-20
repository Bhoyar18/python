

# Inheritance = Inheritance allows us to define a class that inherits all 
# the methods and properties from another class.
# Inheritance is the ability to ‘inherit’ features or attributes from 
# already written classes into newer classes we make.

# Python also has a super() function that will make the child class 
# inherit all the methods and properties from its parent:
# Parent class is the class being inherited from, also called base class or 
# Child class is the class that inherits from another class,
# also called derived class.

class Person:
    def __init__(self, name, age):  # Constructor to initialize name and age attributes
        self.name = name
        self.age = age
    def say_hello(self):  # Method to greet and introduce the person
        print(f"Hello, my name is {self.name} and I am {self.age} years old.")

class Student(Person):  # Student class inherits from Person class
    def __init__(self, name, age, grade):  # Constructor to initialize name, age, and grade attributes
        super().__init__(name, age)  # Call the parent class constructor to initialize name and age
        self.grade = grade  # Additional attribute specific to the Student class

    def say_hello(self):  # Override the say_hello method of the parent class
        super().say_hello()  # Call the parent class say_hello method to introduce the student as a person
        print(f"I am a student in {self.grade}.")  # Print additional information specific to the Student class

# Creating an instance of the base class
person = Person("Vaishnavi", 22)
person.say_hello()

# Creating an instance of the derived class
student = Student("Mandavi", 19, "2nd year")
student.say_hello() 