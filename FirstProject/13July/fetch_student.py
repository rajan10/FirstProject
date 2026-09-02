import sqlite3

connection=sqlite3.connect("student.db")

#create cursor object to execute sql queries
cursor =connection.cursor()
sql="select * from students"
cursor.execute(sql)

students= cursor.fetchall()
print(type(students))

for student in students:
    print(student)