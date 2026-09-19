import sqlite3  # to connect with SQLite db
from config.settings import DB_NAME  # import from /config/settings  .represents the package/module name


# student_repository.py will interact with sqllite like repository file. Database_node.py will select * from table 
# student_repository = Database worker  && node=manager   

def find_student(student_id):

    conn = sqlite3.connect(DB_NAME)  # conn =entering the library   

    """
    row_factory ले database बाट आएको row लाई column name बाट access गर्न सजिलो बनाउँछ।
    Without:
    student[0]
    student[1]

    With:
    Example database
    Suppose:

    student_id	| name	| program
        101	|Raj	| Computer Science

    With sqlite3.Row:
    student["student_id"]
    student["name"]
    student["program"]

    याद गर्ने:
    Row Factory = Database row लाई useful format मा बनाउने factory
    """
    conn.row_factory = sqlite3.Row  # Make rows accessible by column names; conn is like entering the library

    cur = conn.cursor()  # cursor is use to execute sql commands; cursor is like librarian

    data = cur.execute(
        "SELECT * FROM students WHERE student_id = ?",  # ? is a placeholder
        (student_id,)
    )

    return data.fetchone()  # fetch one record/row