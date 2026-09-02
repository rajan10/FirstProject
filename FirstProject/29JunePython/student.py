


class Student:
    def __init__(self, name, age, grade):
        self.name = name
        self.age=age
        self.grade=grade
    inst_name="George Brown college"

    def display_info(self):
        print(f"Name: {self.name}, Age: {self.age}, Grade: {self.grade}")
        print(f"Institute Name: {Student.inst_name}")

s1=Student(name="Alice", age=20, grade="A")
s2=Student(name="Rajan", age=25, grade="B")
s1.display_info()
s2.display_info()
print(f"Institute Name: {Student.inst_name}")
