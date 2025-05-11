'''student={"name":"Bob",
"age":20,
"Branch":"AIML"}
print(student)'''

'''student=dict(name="Bob",
age=20,
Branch="AIML")
#print(student["type"])

#print(student.get("name","not available"))
student["name"]="Lucky"
student["Year"]=2025
#print(student)

#del student["name"]
#print(student)
#student.pop()
#print(student)

student.popitem() 
print(student)'''

'''student=dict(name="Bob",
age=20,
Branch="AIML")
for key in student:
    print(key,":",student[key])'''

'''student=dict(name="Bob",
age=20,
Branch="AIML")
for value in student.values():
    print(value)'''

'''student=dict(name="Bob",
age=20,
Branch="AIML")
for key,value in student.items():
    print(f"{key}->{value}")'''

#nested dictionary
students={
    "student1":{"name":"Hi","age":28},
    "student2":{"name":"Hello","age":29}
}
print(students["student1"]["name"])
print(students["student2"]["name"])