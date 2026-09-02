class Calculator:
    def add(self, a, b):
        return a + b

    def subtract(self, a, b):
        return a - b

    def multiply(self, a, b):
        return a * b

    def divide(self, a, b):
        if b != 0:
            return a / b
        else:
            raise ValueError("Cannot divide by zero.")
        
calc=Calculator()
calc1=calc.add(10,5)
calc2=calc.subtract(10,5)
calc3=calc.multiply(10,5)
calc4=calc.divide(10,5)
print(calc1)
print(calc2)
print(calc3)
print(calc4)