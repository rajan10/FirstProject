class Student:

    inst_name="RAj company"

    def __init__(self,i):
        self.name=i

    def display(self):
        print(self.name, "--",Student.inst_name)

    @staticmethod
    def test():
        print('test')


s1=Student("Rajn")
s1.display()
Student.test()