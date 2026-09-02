x= int(input("Enter the value of x:"))
y= int(input("Enter the value of y:"))
z= int(input("Enter the value of z:"))

if(x>y):
    if(x>z):
        print(x, " is the largest number")
    else:
        print(z," is the largest number")
else:
    if(y>z):
        print(y, "is the largest number")
    else:
        print(z, "is the largest number")


x=int(input("Enter a number:"))
print ("Even no") if (x%2==0) else print("Odd number")