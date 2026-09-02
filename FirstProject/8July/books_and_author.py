class Author:
    def __init__(self,name,gender, nationality, dob):
        self.name=name
        self.gender=gender
        self.nationality=nationality
        self.dob=dob
    def __str__(self):
        return f"Author: {self.name}"
    def hello(self):
        return "hello world"
class Book:
    def __init__(self,name,author, publisher, price):
        self.name=name
        self.author=author
        self.publisher=publisher
        self.price=price 
    def __str__(self):
        return f"Book:{self.name}, {self.author}"
    def get_author(self,):
        return self.author.name
   
ram=Author("Ram prasad", "Male","Nepali","1990/10/10")
jungle=Book("The Jungle Book", ram, "Image Publication", 500)
print(jungle.get_author())
# print(get_author)
# print(jungle)
# print(ram.hello())

