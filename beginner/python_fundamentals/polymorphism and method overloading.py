#polymorphism 
class Dog:
    def sound(self):
        print("Bark")

class Cat:
    def sound(self):
        print("Meow")

def make(animal):
    animal.sound()

d=Dog()
c=Cat()

make(d)
make(c)

#method overloading 
class Number:
    def __init__(self,value): #like constructor, executes automatically when object is created
        self.value=value

    def __add__(self,other): #special dunder method used for extending the init
        return self.value+other.value

n1=Number(10) #object
n2=Number(20)

print(n1+n2)

#inheritance
class Number:
    def __init__(self,value):
        self.value=value

    def __add__(self,other):
        return self.value+other.value

n1=Number(10)
n2=Number(20)

print(n1+n2)

class Animal:
    def eat(self):
        print("Eating")

class Dog(Animal):
    def bark(self):
        print("Barking")

d=Dog()
d.eat()
d.bark()

#Method Overriding
class Animal:
    def sound(self):
        print("Animal sound")

class Dog(Animal):
    def sound(self):
        print("Bark")

a=Animal()
d=Dog()

a.sound()
d.sound()