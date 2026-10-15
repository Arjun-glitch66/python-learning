import json
student={
    "Arjun":90,
    "Ram":80
}
with open("student.json","w") as file: #creates a file student.json with {"Arjun": 90, "Ram": 80}
    json.dump(student,file) #converts dict to json str

with open("student.json","r") as file:
    res=json.load(file)
print(res) #{'Arjun': 90, 'Ram': 80} reads and prints it but the student.json shd be existing 