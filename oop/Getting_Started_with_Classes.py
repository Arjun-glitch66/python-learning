class Market:
    def __init__(self,price,quantity):
        self.price=price
        self.quantity=quantity
    def calc(self):
        return self.price*self.quantity 


m=Market(20,30)
print(m.calc())


