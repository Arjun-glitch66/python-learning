class Item:
    pay=0.8
    def __init__(self,price):
        self.price=price
    def give(self):
        return self.price
item1=Item(500)
print(item1.give())