from functools import reduce
# Higher order functions :The functions which takes other functions as 
# an argument.

# Map Function()= jab saare objects ke upar same operations 
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

# # org_list = [1, 2, 3, 4, 5]
# def cube(num):
#     return num**3
# fin_list = list(map(cube, org_list))
# print(fin_list)

# def add(n):
#     if n<5:
#         return n+2
#     elif n>5:
#         return n*2
# num=(1,2,3,4,5,6,7,8)
# result=map(add,num)
# print(list(result))

# ========================================================================

# Filter = filter function in Python is a built-in function that creates
#  a new list from an existing one, keeping only those elements that satisfy a certain condition.
# numbers=[24,56,78,97,65,43,90]
# def even(n):
#     return n%2==0
# result=filter(even,numbers)
# print(tuple(result))

# numbers=[1,2,3,4,5,6,7,8,9,10,11,12,13]
# def find(num):
#     return num<5 or num>10
# filtered=filter(find,numbers)
# print(list(filtered))

# def hello(n):
#     return n%2==0
# number =[11,12,13,14,1,6]
# # filtered=filter(hello,number)
# # print(tuple(filtered))
#     #      or
# filtered=tuple(filter(hello,number))
# print(filtered)


# Combining Filter with Other Functions =>
# example=[11,12,13,14,15,16,17,18]
# def square(n):
#     return n*n
# number=filter(lambda n:n%2!=0 ,example)
# numbers2=map(square,number)
# print(tuple(numbers2))

# example=[11,12,13,14,15,16,17,18]
# def square(n):
#     return n*n
# number=filter(lambda n:n%2!=0 ,example)
# numbers2=map(square,example)
# print(list(number))
# print(tuple(numbers2))

# nums=[1,2,4,5,6,8,9,10]
# update1=(filter(lambda n:n%2==0,nums))
# update2=(map(lambda n:n+2,update1))
# print(tuple(update2))

# nums=[1,2,4,5,6,8,9,10]
# update1=(filter(lambda n:n%2==0,nums))
# update2=(map(lambda n:n+2,nums))
# print(tuple(update1))
# print(tuple(update2))

# =======================================================================

# Lambda function = They're commonly referred to as anonymous(defined without a name) functions.
# Notice that the anonymous function does not have a return keyword. 
# This is because the anonymous function will automatically return the
# result of the expression in the function once it is executed.
# that can take any number of arguments but, unlike normal functions,
#  evaluates and returns only one expression.

# calc = lambda num: "Even number" if num % 2 == 0 else "Odd number"
# print(calc(20))

# def cube(c):
# 	return c*c*c
# l_cube = lambda c: c*c*c
# print(cube(6))

# ==================================================================

# Reduce = The main purpose of the reduce method is to
# obtain a single outcome from an iterable by implementing some action
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

# factorial = (reduce(lambda x, y: x*y, range(1, 6)))
# print(factorial)

