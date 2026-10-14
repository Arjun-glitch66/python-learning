class Phone:
    def __init__(self,name,qty,price):
        self.name=name
        self.qty=qty
        self.price=price
    def calc(self):
        return self.qty*self.price

class Lap(Phone):
    def __init__(self,name,qty,price,repair):
        super().__init__(name,qty,price)
        self.repair=repair
    def repaired(self):
        self.repair=1 #assigning the value 1 instaed of 2 
        return self.repair
obj=Lap("Arjun",4,500,2)
print(obj.calc())
print(obj.repair) #before it is 2
res=obj.repaired()
print(res) # now after calling the repair() its 1
