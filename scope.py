

#Scope :

#local variable(inside the function(within the block(scope upto the body of function only)) that is y=10)
'''def add(x):
    y=10
    sum=x+y
    print(sum)
add(10)'''


#global variable(outside the function(within the block that is throghout all the page) that is y=20)
'''y=20
def add(x):
    sum=x+y
    print(sum)
add(10)
print(y)'''

'''y=20
def add(x):
    y=10
    sum=x+y
    print(sum)
add(10)
print(y)'''


#global varible ko khi pe bhi access krne ke liye 
#globals()[] method ka use kiya jata hai 
'''y=20
def add(x):
    y=10
    sum=x+globals()['y']
    print(sum)
add(10)
print(y)'''

#local variable ko uske scope ke bhr access krne ke liye 
#global keyword ka use kiya jata hai
'''def add(x):
    global y
    y=10
    sum=x+globals()['y']
    print(sum)
add(10)
print(y)'''


'''y=20
def add(x):
    global y
    y=10
    sum=x+globals()['y']
    print(sum)
add(10)
print(y)'''
#here the value of y will be 10

'''def add(x):
    global y
    y=10
    sum=x+globals()['y']
    print(sum)
    y=20
add(10)
print(y)'''#here the value of y will be 20 due to overriding



'''y=50
def add(x):
    global y
    y=10
    sum=x+y
    print(sum)
    add(x)
print(y)
y=30
print(y)'''

#c
# 
# Calculator programm
# def add(x,y):
#     return x+y
# def sub(x,y):
#     return x-y
# def multi(x,y):
#     return x*y
# def div(x,y):
#     return x/y
# print("Select the operation : ")
# print("1.add")
# print("2.sub")
# print("3.multi") 
# print("4.div")
# n=int(input("enter your choice (1/2/3/4):  "))
# x=int(input("Enter first number : "))
# y=int(input("Enter second number : "))
# if n==1:
#     print(x,"+",y,"=",add(x,y))
# elif n==2:
#     print(x,"-",y,"=",sub(x,y))
# elif n==3:
#     print(x,"*",y,"=",multi(x,y))
# elif n==4:
#     print(x,"/",y,"=",div(x,y))


# map function()= jab saare objects ke upar same operations perform krna hota hai to map function ka use hota hai
# list1=[5,10,15,20,25]
# def add(n):
#     return n+5
# x=map(add,list1)
# print(x)
# print(tuple(x))
# print(list(x))


# my_list=[10,25,30,45,50,65,70,85,23]
# def odd_even(n):
#     if n%2==0:
#         return 'even'
#     else:
#         return 'odd'
# x=list(map(odd_even,my_list))
# print(x)

# filter function()=jb operation kuch item ke upar perform krna ho tb filter function ka use hota hai
my_list=[10,25,30,45,50,65,70,85,90]
def even(n):
    if n%2==0:
       return 'true'
x=list(filter(even,my_list))
print(x)