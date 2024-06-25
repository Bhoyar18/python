

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

# generator way of function
# yeild is keyword which is used to generate generator instance ,
# this can be used in place of return 
def square(num):
    for i in range (1,num+1):
        yield i*i
data=square(10)
for i in data:
    print(i)
