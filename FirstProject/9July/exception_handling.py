a= int(input("Enter 1st number :"))
b= int(input("Enter 1st number :"))

try:
    result =a/b
except ZeroDivisionError:
    print("Can't have zero as divisor")
else:    
    print(result)
print("continue...")