import mysql.connector

def get_connection():
    try:
        connection=mysql.connector.connect(

            host="localhost",
            port=3306,
            user="root",
            passwd="DellKeho#123",
            database="student")
        return connection
    except mysql.connector.Error as error:
        print("Database conn failed:", error)
        return None

def create_table():
    connection=get_connection()
    if connection is None:
        return 
    
    try:
        cursor=connection.cursor()
        sql ="""
        CREATE TABLE IF NOT EXISTS students (
        student_id INT PRIMARY KEY AUTO_INCREMENT,
        student_name VARCHAR(100) NOT NULL,
        student_email VARCHAR(100) UNIQUE NOT NULL,
        student_course VARCHAR(100) NOT NULL,
        student_fee DECIMAL(10,2) NOT NULL
        )
            """
        cursor.execute(sql)
        connection.commit()
    except mysql.connector.Error as error:
        print("Error while creating table,", error)
    finally:
        if cursor:
            cursor.close
        if connection.is_connected():
            connection.close()
        print("connection is closed")

# create_table()
