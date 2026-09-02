class GrandParent:
    def grandparent_method(self):
        return("This is a method from the GrandParent class.")

class Parent(GrandParent):
    def parent_method(self):
        return("This is a method from the Parent class.")

class Child(Parent):
    def child_method(self):
        return("This is a method from the Child class.")

obj=Child()
print(obj.grandparent_method())
print(obj.parent_method())
print(obj.child_method())