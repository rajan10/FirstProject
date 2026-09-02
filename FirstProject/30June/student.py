class Student:
    def __init__(self,name, marks):
        self.name=name
        self.marks=marks

   
    @staticmethod
    def is_pass(marks):
        return marks >= 50
    
    def result(self):
        return Student.is_pass(marks=self.marks)


s1=Student("John", 20)
result=s1.result()
print(result)


