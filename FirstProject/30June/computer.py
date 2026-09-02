class computer:
    def __init__(self,name, model, price):
        self.name=name
        self.model=model
        self.price=price

    def display_info(self):
        print(f"Name: {self.name}")
        print(f"Model: {self.model}")
        print(f"Price: ${self.price:.2f}")
        
    @staticmethod
    def static_method():
        print("This is a static method. It can be called without creating an instance of the class.")

computer1 = computer("Dell", "XPS 15", 1500)
computer1.display_info()
computer.static_method()  # Calling the static method without creating an instance