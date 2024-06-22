# Polymorphism = multiple forms of a single object ,also 
# depends on situation behaviour of that object will change.
# Polymorphism is divided into two categories: 1.Overloading 2.Overriding 
# Overloading = ek hi class ke andar same name ko 2 method banate hai lekin, 
# parameters differnet ho tab is situation ki method overloading bolte hai
# NOTE = python does not support overloading directly ,through
# multiple dispatch python supports overloading   
# class A:
#     def new(self,x=0,y=0,z=0):
#         return x+y+z
# obj=A()
# print(obj.new(5,6))
# print(obj.new(4,8,7))
# print(obj.new(5))

# from multipledispatch import dispatch
# class A:
#     @dispatch(int,int)
#     def add(self,x,y):
#         print(x+y)
#     @dispatch(int,int,int)
#     def add(self,x,y,z):
#         print(x+y+z)
# obj=A()
# obj.add(10,20)
# obj.add(30,40,50)

#Overriding= 2 different class me same name ki method banate hai tb
# isko overriding bolte hai
class A:
    def add(self,a,b):
        print('Output from child class')  
class B(A):
    def add(self,x,y):
        print('Output from child class')
        super().add(30,40)
obj=B()
obj.add(10,20)


# implementing polymorphism using function
class India():
    def capital(self):
        print("New Delhi is the capital of India.")
    def language(self):
        print("Hindi is the most widely spoken language of India.")
    def type(self):
        print("India is a developing country.")
class USA():
    def capital(self):
        print("Washington, D.C. is the capital of USA.")
    def language(self):
        print("English is the primary language of USA.")
    def type(self):
        print("USA is a developed country.")
def func(obj):
    obj.capital()
    obj.language()
    obj.type()
obj_ind = India()
obj_usa = USA()
func(obj_ind)
func(obj_usa)