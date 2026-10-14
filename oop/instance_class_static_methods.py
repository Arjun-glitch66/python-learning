class Item:
    pay=0.8
    def __init__(self,price):
        self.price=price
    def give(self):
        return self.price
item1=Item(500)
print(item1.give())

#class method

class Item:
    def __init__(self,price):
        self.price=price
    @classmethod
    def create_item(cls,price):
        return cls(price) #cls is like self it points to the instance of the object and class respectively

item1=Item.create_cls(500) #automatically creates the object 
print(item1.price)

#class mehtod_2
class Item:
    def __init__(self,name,price):
        self.name=name
        self.price=price
    @classmethod
    def convertion(cls,data):
        name,price=data.split(",")
        return cls(name,int(price))
item1=Item.convertion("Product,100") #converts and also creates the object automatically 
print(item1.name)
print(item1.price)

#static method
class Item:
    def __init__(self,price):
        self.price=price
    @staticmethod
    def expensive(price):
        return price>1000
print(Item.expensive(1500)) #doesnt require objects to access the method 
print(Item.expensive(500))