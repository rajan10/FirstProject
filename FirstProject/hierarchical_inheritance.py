class Parent:
    def parent_method(self):
        print("This is a method from the Parent class.")

class Child1(Parent):
    def child1_method(self):
        print("This is a method from the Child1 class.")

class Child2(Parent):
    def child2_method(self):
        print("This is a method from the Child2 class.")

c1=Child1()
c1.parent_method()
c1.child1_method()
