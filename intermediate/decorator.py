def greet():
    return "HELLO"
def decorator(func):
    def wrapper():
        print("Before")
        func()
        print("After")
    return wrapper
greet=decorator(greet)
greet()

#################
def decorator(func):
    def wrapper(*args, **kwargs):
        print("Starting")
        func(*args, **kwargs)
        print("Finished")
    return wrapper
@decorator
def greet(name):
    print("Hello", name)


greet("Arun") # if we want to pass arguement here we need to keep *args,**kwargs