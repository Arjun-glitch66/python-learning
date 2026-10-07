a=10
b=20

print(a==b)   #False
print(a!=b)   #True
print(a>b)    #False
print(a<b)    #True
print(a>=b)   #False
print(a<=b)   #True

result=10>5

print("Result: ",result)
print(type(result))

a = 15
b = 4

# Arithmetic
print(a + b)
print(a / b)
print(a // b)
print(a % b)
print(a ** 2)

# Comparison
print(a > b)
print(a == b)

# Boolean
print(a > 10 and b < 5)
print(a < 10 or b < 5)

# Membership
numbers = [10, 20, 30, 40]

print(20 in numbers)
print(50 not in numbers)

# Ternary
result = "Big" if a > 10 else "Small"
print(result)

name = "Arjun Kumar"

# Basic
print(name)
print(len(name))

# Characters
print(name[0])
print(name[-1])

# Slicing
print(name[0:5])
print(name[:5])
print(name[6:])

# String methods
print(name.upper())
print(name.lower())

# Replace
print(name.replace("Kumar", "SRM"))

# Find
print(name.find("Kumar"))

# Reverse
print(name[::-1])

# Split
words = name.split()
print(words)


#strings are immutable so only like this we can do 
name2="Arjun"
name2="B"+name2[1:]
print(name2)