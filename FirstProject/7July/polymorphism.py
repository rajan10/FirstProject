class Dog:
    def sound(self):
        print("Dog barks")

class Cat:
    def sound(self):
        print("Cat meows")

def animal_sound(animal=Dog):
    animal.sound()

animal_sound(animal=Dog())
animal_sound(animal=Cat())