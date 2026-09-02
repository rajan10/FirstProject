import sqlite3

connection=sqlite3.connect("student.db")
cursor =connection.cursor()
student_name = input("Enter name:")
student_email = input("Enter Email:")
student_course = input("Enter Student course:")
student_fee = input("Enter student fee:")

sql= "insert into students(student_name, student_email,student_course, student_fee) values(?,?,?,?)"

cursor.execute(sql,(student_name,student_email,student_course,student_fee,))
                
connection.commit()
connection.close()