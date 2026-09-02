
try:
    a=int(input("Enter first number :"))
    b=int(input("Enter first number :"))
    result = a / b
    print("Result :", result)

except ValueError as ve:
    print("Pls enter numbers", ve)

except ZeroDivisionError as zd:
    print("Don't enter zeros", zd)

except Exception as e:
    print("Exception occured", e)

print("Done")