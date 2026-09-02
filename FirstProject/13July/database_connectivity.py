import sqlite3

connection=sqlite3.connect("student.db")
cursor =connection.cursor()
cursor.execute("""
               create table if not exists students(student_id integer primary key autoincrement,
               student_name text,
               student_email text unique,
               student_course text,
               student_fee REAL
)
""")
                
connection.commit()
connection.close()
