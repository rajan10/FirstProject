class Student:
    def __init__(self, student_id, name):
        self.student_id = student_id
        self.name = name
        self.courses = []
        self.payments = []

    def enroll_course(self, course):
        self.courses.append(course)
        print(f"{self.name} has enrolled in {course.course_name}.")

    def make_payment(self, course, amount):
        if course not in self.courses:
            print(f"{self.name} is not enrolled in {course.course_name}. Cannot process payment.")
            return False
        
        if amount <= 0:
            print("Payment amount must be greater than zero.")
            return False
        
        if amount > course.course_fee:
            print(f"Payment amount exceeds the course fee of ${course.course_fee}.")
            return False
        
        balance = course.course_fee - amount
        self.payments.append((course.course_name, amount))
        print(f"Payment of ${amount} made for {course.course_name}. Remaining balance: ${balance}.")
        return True