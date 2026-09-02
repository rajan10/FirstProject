import sqlite3
connection = sqlite3.connect("student.db")
cursor = connection.cursor()

student_id=input("Enter Student_id to delete:")
sql= "DELETE from students where student_id =?"
cursor.execute(sql,(student_id,))

connection.commit()
connection.close()
print("Record deleted successfully!")