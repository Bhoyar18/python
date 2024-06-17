
#Function = block of code jo baar baar apne code me likhna pd rha hai usko 
#function ke andr rakh ke use kr skte instead baar likhne ki jgh 
#Instead of repeatedly creating the same code block for various input variables,
# we can call the function and reuse the code it contains with different variables.
#Once defined, Python functions can be called multiple times and from any location in a program.

# two types of functions
#1.in-built functions= jo functions ne python ne khud bnake diye hai(functions which are 
# coming along with Python software automatically)
#print(),min(),max(),sum(),type(),id(),str(),float(),complex(),len(),eval()

#2. user-defined functions = jo functions ham khud bnake use krte hai(The functions which are 
# defined by the developer as per the requirement are called user-defined functions)

# def - this is a key word is used to create a function

#kisi function ko banate  time parameter use krte hai aur kisi function ko call krte time argumnet ka use krte hai

#different ways to write and print function

#1.
'''def add(x,y):#x,y=parameters
    z=x+y
    return z
a=add(10,20)#in place of a koi bhi value le skte hai ,10,20=arguments
print(a)
'''

#2.
'''def add(x,y):
    z=x+y
    return z
p=int(input("Enter first value : "))
q=int(input("Enter second value : "))
r=add(p,q)
print(r)'''

#3.
'''def add(x,y):
    z=x+y
    print(z)
p=int(input("Enter first value : "))
q=int(input("Enter second value : "))
add(p,q)'''

#4.
#jab bhi print ek hi line me 1 se jada baar use ho jaay tb 
#ouput ke saath None bhi return krega
'''def add(x,y):
    z=x+y
    print(z)
p=int(input("Enter first value : "))
q=int(input("Enter second value : "))
print(add(p,q))'''
#output = 
#Enter first value : 10
#Enter second value : 10
#20
#None

'''x=50
print(print(print(x)))
output=
50
None
None'''



'''def add(x,y):
    z=x+y
    print(z)
p=int(input("Enter first value : "))
q=int(input("Enter second value : "))
a=add(p)
print(p)'''
#this will give error beacause in a we have only pass one argument thats is p
#we didnt pass q
#TypeError: add() missing 1 required positional argument: 'y'

'''def add(x=0,y=0):
    z=x+y
    return z
p=int(input("Enter first value : "))
q=int(input("Enter second value : "))
a=add(p)
print(a)'''
#this will not give any error because we have passed the default values that is 0,
#it will automatically print the value of p which is given by us
# because in a we have pass add(p)


'''def square(x):
    square=x**x
    return square
z=int(input("Enter any number : "))
p=square(z)
print(p)'''


'''def add(*x):
    add=0
    for i in x:
        add=add+i
    print(add)
add(10,20)
add(10,20,30,40,50,60,70)'''


'''def employee_data(**data):
   for i,j in data.items():
    print(i,"=",j)
    print(j)
employee_data(name="Vaishu",age="21")'''

#square
'''def square(x):
    print("Square of",x," =", x*x)
square(4)
square(5)'''


# even odd
# def even_odd(x):
#     if x%2==0:
#         print("even")
#     else:
#         print("odd")    
# even_odd(90)
# even_odd(91)



# factorial of any number
# def factorial(num):
#     result=1
#     while num>=1:
#         result=result*num
#         num=num-1
#     return result    
# i=int(input("Enter any number : "))
# print(factorial(i))

# def add_sub(a,b):
#     add=a+b
#     sub=a-b
#     return add,sub
# x,y=add_sub(100,40)
# print(x)
# print(y)

#   OR

# def add_sub(a,b):
#     add=a+b
#     sub=a-b
#     return add,sub
# x,y=int(input("Enter first number : ")),int(input("Enter second number : "))
# print(x+y)
# print(x-y)

def calc(a,b):
    add=a+b
    sub=a-b
    mul=a*b
    div=a/b
    return add,sub,mul,div
x,y,z,p=calc(int(input("Enter first value : ")),int(input("Enter second value : ")))
print("Addition is = ",x)
print("Subtraction is = ",y)
print("Multiplication is = ",z)
print("Division is = ",p)


