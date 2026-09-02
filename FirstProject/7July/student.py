class Student:
    id=10
    name="Raj"

    def talk(self):
        print(hash(self))
        print("Stduent talks")

s1=Student();
s1.talk()
s2=Student();
s2.talk()
print(hash(s1))
print(hash(s2))