import sqlite3

connection=sqlite3.connect("student.db")
cursor =connection.cursor()

student_id = int(input("Enter studet id: "))

sql= "select * from students where student_id =?"
cursor.execute(sql,(student_id,))

student= cursor.fetchone()
print(student)