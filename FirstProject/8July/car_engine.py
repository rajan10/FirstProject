class Engine:
    def __init__(self,hp):
        self.hp=hp

class Car:
    def __init__(self,brand, engine):
        self.brand=brand
        self.engine=engine

    def get_engine(self):
        return self.engine.hp
  
c1=Car("Toyota",Engine(1000))   

print(c1.get_engine())

