

# Decorator = These are used to modify the behavior of the function.
#  Decorators provide the flexibility to wrap another function to 
# expand the working of wrapped function, without permanently modifying it.


def decorator(x):
    def wrapper():
        print("Start work")
        x()
        print("Stop Work")
    return wrapper
@decorator
def originalfun():
    print("This is original function ")
originalfun()

