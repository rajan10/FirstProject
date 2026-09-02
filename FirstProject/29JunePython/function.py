def function_name():
    print('hello world!')
function_name()

def wish(name):
    print("hello", name,"Good morning!")

wish("Rajan")


def print_student_data(name,course):
    print("Student name is:", name)
    print("Student course is:", course)
print_student_data("Rajan","Python")
print_student_data(course="Java", name="Saajan")


def print_student_data(name,course="GEN AI"):   
    print("Student name is:", name)
    print("Student course is:", course)

print_student_data(name="Harish")
print_student_data("Smitha")


def add(a,b):
    return a+b

result = add(10,20)
print("Addition is:", result)


#function
def login():
    pass


#Variable length arguments
# add(a,b)
# add(a,b,c)

def print_numbers(*args):
    print(args)

print_numbers(10,20)

def print_numbers(*i):
    print(i)

print_numbers(10,20,30,40,50)

def student_info(**args):
    print(args)


student_info(name="Rajan", course="Python", age=20)
student_info(name="Saajan", course="Java", age=22, city="Delhi")
student_info(name="Harish", course="C++", age=21, city="Mumbai", country="India")

