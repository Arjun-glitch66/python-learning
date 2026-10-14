my_list=[10,20,30]
my_tuple=(10,20,30)

print(my_list)
print(my_tuple)

###############
nums[0]=99 #error in tuple becuase tuple is immutable 
##############a=(10,20,30)
b=("Phone","Laptop","Tablet")
c=()

print(a[0])   # 10
print(a[-1])  # 30
print(a[1:3]) # (20, 30)
print(len(a)) # 3

###########tuple without paranthesis
a=10,20,30

print(a)        # (10, 20, 30)
print(type(a))  # <class 'tuple'>

###############a=(10)
b=(10,)

print(type(a))  # <class 'int'>
print(type(b))  # <class 'tuple'>

student=("Arjun",20,9.92)# packing

#unpacking
name,age,cgpa=("Arjun",20,9.92)

print(name)
print(age)
print(cgpa)

#asterisk
a,*b,c=(10,20,30,40,50)

print(a)  # 10
print(b)  # [20, 30, 40] #asterisk gives list
print(c)  # 50