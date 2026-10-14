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

