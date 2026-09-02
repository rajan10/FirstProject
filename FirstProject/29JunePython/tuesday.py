#local variable

def test():
    msg1="Hello"
    print(msg1)

test()
#print(msg1)  # This will raise an error because msg1 is a local variable and not accessible outside the function
text= "Welcome to AI Training"
def test1():
    print(text)

test1()
print(text)  # This will work because text1 is a global variable and accessible outside the function