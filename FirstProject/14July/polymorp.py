
# Duck Typing: Polymorphism, one interface many behaviors(forms)
# There are 2 types of Polymorphism. 1) Runtime Polymorphism (Inheritance: Method Overriding)
# 2) Duck Typing (No inheritance needed)
class Dog:
    def sound(self):
        print("Dog Barks....")
class Cat:
    def sound(self):
        print("Cat meows")
class Human:
    def sound(self):
        print("Human speaks")
def animal_sound(animal): #Does this object has sound()... I don't care 
# where it came from as long as there is sound()
    animal.sound()

dog = Dog()
cat = Cat()
human =Human()

animal_sound(Human())
