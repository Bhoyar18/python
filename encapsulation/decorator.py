

# Decorator = These are used to modify the behavior of the function.
# Decorators provide the flexibility to wrap another function to 
# expand the working of wrapped function, without permanently modifying it.
# def decorator(x):
#     def wrapper():
#         print("Start work")
#         x()
#         print("Stop Work")
#     return wrapper
# @decorator
# def originalfun():
#     print("This is original function ")
# originalfun()

# def decorator(fun):
#     def wrapper():
#         print("Transaction Started")
#         fun()
#         print("Transaction Completed")
#         return wrapper
# @decorator
# def hello():
#     print("Execution.......")
# hello()

# def one(a,b):
#     print(a/b)
# def new_one(func):
#     def two(a,b):
#      if a<b:
#         a,b=b,a
#      return func(a,b)
#     return two
# obj=new_one(one)
# one(10,5)


        






# generator way of function
# yeild is keyword which is used to generate generator instance ,
# this can be used in place of return 
def square(num):
    for i in range (1,num+1):
        yield i*i
data=square(10)
for i in data:
    print(i)
