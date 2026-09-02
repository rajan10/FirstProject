class Student:
    def __init__(self,name,marks):
        self.name=name
        self.marks=marks
    def calculate_average(self):
        total_marks=0
        for i in self.marks:
            total_marks=total_marks+i
        average_marks=total_marks/6
        return average_marks  
    def calculate_grade(self, average_marks123):
        if average_marks123>=80:
            return "Grade:A"
        elif average_marks123>=70:
            return "Grade:B"
        elif average_marks123>=60:
            return "Grade:C"
        else:
            return "Fail"      
ram=Student("Ram",[80,90,80,87,66,88])
sita=Student("Sita",[10,12,30,17,26,48])
ram_average=ram.calculate_average()
print(ram_average)
ram_grade=ram.calculate_grade(ram_average)
print(ram_grade)
sita_average=sita.calculate_average()
print(sita_average)
sita_grade=sita.calculate_grade(sita_average)
print(sita_grade)