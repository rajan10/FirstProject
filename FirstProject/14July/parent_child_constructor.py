class Parent:
    def __init__(self):
        print("Parent constructor")
        self.bike="Spledor..."
        self.cash=5000
    
    def display(self):
        print("Parents bike ")
        print("Parents Cash ")


class Child(Parent):
    def __init__(self):
        print("child constructor")
        super().__init__()
        self.bike="Royal Enfield"
        self.cash="10000"

obj=Child()
obj.display()