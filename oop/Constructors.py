class Item:
        def __init__(self,price:float,name:str,quantity=0): #type hints are for user clarification it doesnt affect at runtime
            assert price>=0, f" {price} is negative reinput the value" #AssertionError statement 
            assert quantity>=0, f"{quantity} is negative reinput the value"

            self.price=price
            self.name=name
            self.quantity=quantity

        def calc(self):
            print(self.name)
            return self.price*self.quantity

item1=Item(500,"Arjun",2)
item2=Item(600,"Rahul") #default quantity value 0 assigned
print("1")
print(item1.calc())
print("2")
print(item2.calc())
