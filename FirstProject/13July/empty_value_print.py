

employee ={

    "name":"Raj",
    "salary":None,
    "department": "",
    "skills":[],
    "active": True
}
""" for key,value in employee.items():
    if not employee[key]:
        print(f"{key} ---> {value!r}") """


""" x=" "
print(repr(x)) """

""" def hello():
    print("Hello")
    

x= hello()
print(x) """

def add():
    return 10

print(add())

a=None
b=None
c =None
print(id(a))
print(id(b))
print(id(c))