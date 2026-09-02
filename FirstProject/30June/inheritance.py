class Parent:
    def house(self):
        print("Parent has a house.")

class Child(Parent):
    def bike(self):
        print("Child has a bike.")

c=Child()
c.bike()
c.house()  # Accessing the inherited method from Parent class