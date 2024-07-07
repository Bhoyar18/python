  

#print("...hello world...")

# variable=a container to hold the value
'''vaishu=10
_vaishu=20
print(vaishu)
x,y,z=10,20,30
print(x)
print(y)
print(z)'''

#x=y=z=10
#print(x) #=this is used for single line comment(ctl+/)and also this is called single line comment
'''print(y) this('''''') triple code is used for multiple line comment 
print(z)'''

#to find python keywords
'''import keyword
print("The list of keywords is : ")
print(keyword.kwlist)'''

#Assign Multiple Values in multiple variables in single line:-
'''x, y, z = "Vaishu", "Maanu", "Vaishu"
print(x)
print(y)
print(z)
'''
#One Value to Multiple Variables in single line:
'''x = y = z = "vaishu"
print(x)
print(y)
print(z)
'''

'''city = ["Bhopal", "Indore", "Jabalpur"]
x, y, z = city
print(x)
print(y)
print(z)'''

#string
'''str="python"
print(type(str))'''





# str2 = 'JAVA proGramming laNGuage.'
# print(str2.center(70,'@'))

# x=range(0,10,2)
# print(list(x))
# print(tuple(x))

# x=range(-1,-10,-1)
# print(list(x))
# print(tuple(x))

# x=range(1,11,-1)
# print(list(x))
# print(tuple(x))


# def square(num):
#     for i in range (1,num+1):
#         print(i*i)
# square(10)



#Q1.
# Lambda=They're commonly referred to as anonymous(defined without a name) functions.
# Notice that the anonymous function does not have a return keyword.
# they can take any number of arguments but,returns only one expression.
# example=>
# calculate = lambda num: "Even number" if num % 2 == 0 else "Odd number"
# print(calculate(21))

# #Q4.
# my_list=[2,4,6,8,10,12,14,16]
# def add(n):
#     return n+5 
# output=list(map(add,my_list))
# print(output)

# # Q5.
# my_list=[1,2,3,4,5,6,7,8,9,10]
# def odd(n):
#     if n%2!=0:
#         return 'odd'
# output=list(filter(odd,my_list))
# print(output)

# # Q6.
# from functools import reduce
# my_list=[10,5,25,30,25,65,35,40,50,45]
# def sum(a,b):
#     return a+b
# output=reduce(sum,my_list)
# print(output)

# # Q3.
# # generator (yeild is keyword which is used to generate generator instance ,
# # this can be used in place of return) 
# def square(num):
#     for i in range (1,num+1):
#         yield i*i
# data=square(10)
# for i in data:
#     print(i)

# Q2.
# decorator= Decorator is used to modify thr actual program,without
# changing the actual code.It is required beacause with the help of
# decorator we dont  need to many changes in the code,we just need to 
# @decorator and our code will be enhanced.
# example=>
# def decorator(fun):
#     def wrapper():
#         print("Transaction Started")
#         fun()
#         print("Transaction Completed")
#     return wrapper
# @decorator
# def hello():
#     print("Execution.......")
# hello()
