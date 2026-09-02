import mysql.connector

def get_connection():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        passwd="DellKeho#123",
        database="pydb"
    )

def create_table():
    connection=get_connection()
    cursor=connection.cursor()
    query ="""
CREATE TABLE IF NOT EXISTS STUDENTS(ID INT AUTO_INCREMENT PRIMARY_KEY,
NAME VARCHAR(100) NOT NULL, 
COURSE VARCHAR(100)NOT NULL,
FEE DEDCIMAL(10,2)NOT NULL)
"""
    cursor.execute(query)
    connection.commit()
    cursor.close()
    print("Student table is ready ....")