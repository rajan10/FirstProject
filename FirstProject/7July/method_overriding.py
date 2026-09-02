class Parent:
    def display(self):
        print("parent display method")

class Child(Parent):
    def display(self):
        super().display()
        print("Child Display")

obj= Child()
obj.display()