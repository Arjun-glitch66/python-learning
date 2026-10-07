# Dictionary
student = {
    "name": "Arjun",
    "age": 20,
    "cgpa": 9.92
}

print(student["name"])
print(student["cgpa"])

# Add
student["department"] = "CSE"

# Change
student["age"] = 21

# Check
print("name" in student)
print("Before pop")
print(student.items())
student.pop("cgpa")
print("After pop")
print(student.items())
# Keys and values
print(student.keys())
print(student.values())