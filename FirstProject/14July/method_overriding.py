class Parent:
    def cash(self):
        print("Parents cash")

    def bike(self):
        print("Parents bike (Splendor .....)")

class Child(Parent):
    def bike(self):
        super().bike()
        # print("Child bike (Royal Enfield)........")
obj = Child()

Parent.bike(obj)