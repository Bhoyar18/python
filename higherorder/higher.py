from functools import reduce
# Higher order functions :The functions which takes other functions as an argument

# map function()= jab saare objects ke upar same operations 
# perform krna hota hai to map function ka use hota hai
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

# org_list = [1, 2, 3, 4, 5]
# def cube(num):
#     return num**3
# fin_list = list(map(cube, org_list))
# print(fin_list)

# Filter = filter function in Python is a built-in function that creates
#  a new list from an existing one, keeping only those elements that satisfy a certain condition.
# numbers=[24,56,78,97,65,43,90]
# def even(n):
#     return n%2==0
# result=filter(even,numbers)
# print(tuple(result))

numbers=[1,2,3,4,5,6,7,8,9,10,11,12,13]
def find(num):
    return num<5 or num>10
filtered=filter(find,numbers)
print(list(filtered))


# lambda function = They're commonly referred to as anonymous(defined without a name) functions.
# Notice that the anonymous function does not have a return keyword. 
# This is because the anonymous function will automatically return the
#  result of the expression in the function once it is executed.
# that can take any number of arguments but, unlike normal functions,
#  evaluates and returns only one expression.
# calc = lambda num: "Even number" if num % 2 == 0 else "Odd number"
# print(calc(20))

# def cube(c):
# 	return c*c*c
# l_cube = lambda c: c*c*c
# print(cube(6))


# reduce = 
# my_list=[12,34,56,78,90,89]
# def max(x,y):
#     if x>y:
#         return x
#     else:
#         return y
# x=reduce(max,my_list)
# print(x)   


# my_list=[12,34,56,78,90,89]
# def max(x,y):
#     if x<y:
#         return x
#     else:
#         return y
# x=reduce(min,my_list)
# print(x)   


# my_list=[12,34,56,78,90,89]
# def sum(x,y):
#         return x+y
# x=reduce(sum,my_list)
# print(x)    

# n=int(input("Enter any number"))
# def fact(x):
#      return x*x-1
# x=reduce()
# print(x)

