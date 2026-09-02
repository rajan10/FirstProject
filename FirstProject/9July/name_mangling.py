class Animal:
    def __init__(self):
        self.__value="animal"


class Dog(Animal):
    def __init__(self):
        self.__value="Dog"


d= Dog()
print(d.__dict__)