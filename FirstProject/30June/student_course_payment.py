def process_payment(student_name, course_fee, amount):

    def validate_payment():
        if amount <=0:

            return False
        if amount>course_fee:
            return False
        return True
    
    def calculate_balance():
        return course_fee - amount
    
    def generate 
    # Simulate payment processing logic
    print(f"Processing payment for Student ID: {student_id}, Course ID: {course_id}, Amount: ${amount}")
    # Here you can add actual payment processing code (e.g., API calls to a payment gateway)
    return True  # Return True if payment is successful