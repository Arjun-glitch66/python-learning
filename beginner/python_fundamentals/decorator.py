def decorator(func):
    def wrapper():
        print("Start")
        func()
        print("End")
    return wrapper

@decorator #study=decorator(study)
def study():
    print("Python")

study()
#The original study function is passed into the parameter func, . Return wrapper and assign it to study