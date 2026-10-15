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
    