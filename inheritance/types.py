
# Types of Inheritance
# 1.SINGLE INHERITANCE = Single Inheritance is the simplest form of 
# inheritance where a single child class is derived from a single parent class

# class Parent:                  
#     # parent class
#     def hello1(self):
#         print("This is Parrent Class")
# class Child(Parent):    
#   # child class
#     def hello2(self):               
#         print("This is Child Class")                            
# a = Child()                 
# a.hello1()                 
# a.hello2()         

# 2.MULTIPLE INHERITANCE = In multiple inheritance, a single child 
# class is inherited from two or more parent(base) classes. It means the 
# child(derived) class has access to all the parent classes' methods and attributes.
class Grandparent: 
    house = 'Three storeyed building' 
    def age(self, number): 
        if number>70: 
            return ('Much Older!') 
        else: 
            return ('Growing towards Old age.')        
class Parent: 
    car = 'Swift' 
    def work(self, hours): 
        if hours>40: 
            return ('Very hard working!') 
        else: 
            return ('Average hard working!') 
class Child(Parent, Grandparent): 
    phone = 'Vivo'  
child_object = Child() 
print('My house is a ',child_object.house, ' and I have a ', child_object.car, 
      ' and a ', child_object.phone,' phone.') 
print('My grandparent is 78 years old. He is ', child_object.age(78)) 
print('My father works for 47 hours a week. He is ', child_object.work(47))
