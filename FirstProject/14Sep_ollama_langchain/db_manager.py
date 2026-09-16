"""
db_manager.py
This file handles MySQL database operations.
यो file ले MySQL database सँग connection गर्छ
र courses_info बाट course data ल्याउँछ।
"""
import os

from dotenv import load_dotenv  
from sqlalchemy import create_engine, text 
#sqlalchemy is used to communicate with db
# ---------------------------------------------------------
# Load environment variables
# ---------------------------------------------------------
load_dotenv()
# .env बाट MySQL connection string पढ्छ
MYSQL_URI = os.getenv("MYSQL_URI")
# ---------------------------------------------------------
# Check MYSQL_URI
# ---------------------------------------------------------
if not MYSQL_URI:
    raise ValueError(
        "MYSQL_URI is missing.Please create a .env file."
    )
# ---------------------------------------------------------
# Create MySQL engine
# ---------------------------------------------------------
engine = create_engine(
    MYSQL_URI,
    pool_pre_ping=True  # if in pool connections, pre_ping & if still alive connect to that conn
)
# engine is responsible for connecting Python to MySQL.
# engine ले Python र MySQL बीच connection manage गर्छ।
# ---------------------------------------------------------
# Create course_info table
# ---------------------------------------------------------
def create_courses_table():
    sql = """
    CREATE TABLE IF NOT EXISTS course_info (
        id INT AUTO_INCREMENT PRIMARY KEY,
        course_code VARCHAR(20)
            NOT NULL UNIQUE,
        course_name VARCHAR(150)
            NOT NULL,
        description TEXT,
        duration_months INT,
        fee DECIMAL(10,2)
    )
    """
    # Database connection खोल्छ
    with engine.begin() as connection:
        # SQL statement execute गर्छ
        connection.execute(text(sql))
# ---------------------------------------------------------
# Get courses
# ---------------------------------------------------------
def get_courses():
    sql = """
    SELECT
        course_code,
        course_name,
        description,
        duration_months,
        fee
    FROM course_info
    ORDER BY course_code
    """
    with engine.connect() as connection:
        result = connection.execute(
            text(sql)
        )
        # Database rows लाई dictionary मा convert गर्छ
        rows = result.mappings().all() # maps to dict
    return [dict(row)for row in rows] #list comprehension which converts each row into normal Python dict
# for = one by one
# DICT =put into a labeled box
# ---------------------------------------------------------
# Convert courses into LLM-readable text
# ---------------------------------------------------------
def get_courses_context():
    courses = get_courses() #in dict form
    if not courses:
        return (
            "No course information is currently available."
        )
    course_text = []
    for course in courses:
        text_block = f"""
        Course Code: {course['course_code']}
        Course Name: {course['course_name']}
        Description: {course['description']}
        Duration: {course['duration_months']} months
        Fee: ${float(course['fee']):.2f}
        """
        course_text.append(text_block.strip())
    # IMPORTANT:
    # return must be OUTSIDE the for loop
    return "\n\n".join(course_text)

"""
Course Code: CS101
Course Name: Python Programming
Duration: 3 months
Fee: $750.00

Course Code: CS102
Course Name: Java Programming
Duration: 2 months
Fee: $850.00

Course Code: CS103
Course Name: JavaScript Programming
Duration: 3 months
Fee: $950.00

Course Code: CS104
Course Name: GenAI Programming
Duration: 4 months
Fee: $1000.00
"""