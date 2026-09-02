

# num=int(input("Enter a number: "))
# if num%2==0:
#     print(f" {num} is an even number.")
# else:
#     print(f" {num} is an odd number.")

# class EvenOdd:
#     def check_even_odd(self, num):
#         if num % 2 == 0:
#             return f"{num} is an even number."
#         else:
#             return f"{num} is an odd number."
    
# even_odd_checker = EvenOdd()
# print(even_odd_checker.check_even_odd(500))

class EvenOdd:
    def __init__(self):
    def check_even_odd(self, num):
        if num % 2 == 0:
            return f"{num} is an even number."
        else:
            return f"{num} is an odd number."
    
even_odd_checker = EvenOdd()
print(even_odd_checker.check_even_odd(500))
