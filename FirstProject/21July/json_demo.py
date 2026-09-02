import json

# student object in the dictionary form
student= {
    "id": 101,
    "name":"Ravi",
    "course":"Python",
    "fee":15000
}

student_json=json.dumps(student, sort_keys=True, indent=4)
print(type(student))
print(student_json)
print(type(student_json))

print("--------------------------")
student_object=json.loads(student_json)
print(student_object)
print(type(student_object))
print("--------------------------")
with open("student.json", "w") as file:
    json.dump(student, file, indent=4)

with open("student.json", "r") as file:
    print(file)

