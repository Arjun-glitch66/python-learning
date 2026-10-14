#double mangling
class Item:
    def __init__(self,name):
        self.__name=name
item1=Item("Phone")
print(item1._Item__name) #item1.__name throws error 

#encapsulation, controlling how the data is accessed or changed.
class Item:
    def __init__(self,name):
        self.__name=name
    @property
    def name(self):
        return self.__name #no need to use name() to call it becuase it is treated as attribute because of @property
    
    def set(self,value,user):
        if user!="admin":
            raise PermissionError("Only admin can change the name")
        if len(value)>10:
            raise ValueError("Name is too long")

        self.__name=value
obj=Item("Phone")
obj.set("Laptop","admin")
print(obj.name) #no need for name() since it is @property

#abstraction, hiding unnecessary part

class Item:
    def __init__(self,price,quantity):
        self.price=price
        self.quantity=quantity
    def calc(self):
        return self.price*self.quantity

item1=Item(100,5)
print(item1.calc())

#polymorphism
class Phone:
    def calc(self):
        return 1000*2

class Laptop:
    def calc(self):
        return 2000*3

items=[Phone(),Laptop()]

for item in items: #first iteration item=Phone()
    print(item.calc())