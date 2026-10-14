marks = {"Maths": 90, "Python": 95}
#dict is mutable
print(marks["Python"])  # 95
print(marks.get("Java"))       # None .get() i used becasue if the key java is not available it returns None instead of error   
print(marks.get("Java", 0))    # 0 is the default value so the op is 0 

##############
student = {"name": "Arjun", "age": 20}

# Add a new key-value pair
student["city"] = "Chennai"

# Update an existing value
student["age"] = 21

print(student) #{'name': 'Arjun', 'age': 21, 'city': 'Chennai'}

##################
student = {"name": "Arjun", "age": 20, "city": "Chennai"}

del student["city"]
print(student)
age = student.pop("age")
print(age)
print(student) 
#op
#{'name': 'Arjun', 'age': 20}
#20
#{'name': 'Arjun'}
########################
for key in student: #dictionery by default returns the key in looping studnet.keys() will aslo work
    print(key)
for value in student.values(): #deefault it gives keys only therefore explicilty mention values()
    print(value)
for key, value in student.items():
    print(key, value)

################
#dsa question
num=[1,2,2,1,4]
def count():
    dict={}
    for n in num:
        if n in dict:
            dict[n]=dict[n]+1
        else:
            dict[n]=1
    return dict
res=count()
print(res) #{1:2, 2:2, 4:1}