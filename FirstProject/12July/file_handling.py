import os
with open("students.txt","r")as file:
    data=file.read()
    print(data)

with open("courses.txt", "w") as file:
    file.write("Java\n")
    file.write("Python\n")
    file.write("GEN AI\n")

if os.path.exists("students.txt"):
    pass


# os.rename("courses.txt", "raj-courses.txt")
# os.mkdir("reports")

with open("students.txt", "w+")as file:
    file.write("101-Raj \n102-Ran\n)")
    print("File pointer position: ", file.tell())
    file.seek(0)
    print(file.read())
  
