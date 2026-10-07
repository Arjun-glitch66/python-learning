# User input
name = input("Enter your name: ")
age = int(input("Enter your age: "))

# Control statement
if age >= 18:
    print(f"{name} is an adult")
else:
    print(f"{name} is a minor")

# List
marks = [85, 90, 78, 95]

print(marks)
print(marks[0])
print(marks[-1])

# Add
marks.append(88)

# Change
marks[0] = 100

# Remove
marks.pop()

print(marks)
print(len(marks))