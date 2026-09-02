

class Employee:
    employee_count=0
    def __init__(self, emp_name, role):
        self.emp_name=emp_name
        self.role =role
        self.employee_id= self.generate_employee_id()

    def generate_employee_id(self):
        Employee.employee_count=Employee.employee_count+1
        return f"EMP{Employee.employee_count:03d}"
    
    def __str__(self):
        return f"Employee_Name: {self.emp_name},  Emp Role: {self.role}, Emp_ID: {self.employee_id}"

emp1=Employee("Raj","Developer")
emp2=Employee("Smiron","Python Developer")
print(emp1.employee_id)
print(emp2.employee_id)
print(emp2)