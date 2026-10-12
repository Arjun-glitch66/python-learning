class Student:
    def __init__(self,name,roll): #this is a construdstor parametrised seld vaiirbale refers to current object which is non negotiable
        self.name=name
        self.roll=roll
    def display(self):
        print(self.name)
        print(self.roll)
s1=Student("Arjun",274)
s1.display()

