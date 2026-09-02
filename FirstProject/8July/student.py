class Student:
    def __init__(self, a, b, c,d):
        self.id=a
        self.name=b
        self.course=c
        self.marks=d

    def display_result(self):
        if self.marks> 35:
            return "passed"
        
        return "Fail"

s1=Student(101,"Raj","Python", 25)
s1.new_attribute="new attribute"
result=s1.display_result()
print(result)
print(s1.__dict__)