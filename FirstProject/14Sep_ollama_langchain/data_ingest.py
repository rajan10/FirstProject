"""
data_ingest.py
This file inserts sample courses into MySQL.
नेपाली:
यो file ले courses_info table मा sample course data
insert गर्छ।
"""
from importlib import import_module

text = import_module("sqlalchemy").text
from db_manager import (
    engine,
    create_courses_table
)
# ---------------------------------------------------------
# Sample course data
# ---------------------------------------------------------
COURSES = [

    (
        "CS101",
        "Python Programming",
        "Learn Python programming from beginner to intermediate level.",
        3,
        750.00
    ),
    (
        "AI201",
        "Generative AI Fundamentals",
        "Learn LLMs, prompt engineering, RAG and AI applications.",
        4,
        1200.00
    ),
    (
        "SEC301",
        "Cybersecurity Fundamentals",
        "Learn networking, security fundamentals, threats and defense.",
        4,
        1100.00
    ),
    (
        "DB401",
        "Database Management",
        "Learn SQL, relational databases and database design.",
        3,
        800.00
    )
]
# ---------------------------------------------------------
# Insert courses
# ---------------------------------------------------------
def seed_courses():
    # First make sure table exists
    create_courses_table()
    sql = """
    INSERT INTO course_info
    (
        course_code,
        course_name,
        description,
        duration_months,
        fee
    )
    VALUES
    (
        :code,
        :name,
        :description,
        :months,
        :fee
    )
    ON DUPLICATE KEY UPDATE
        course_name = VALUES(course_name),
        description = VALUES(description),
        duration_months = VALUES(duration_months),
        fee = VALUES(fee)
    """
    with engine.begin() as connection:
        for course in COURSES:
            connection.execute(
                text(sql),
                {
                    "code": course[0],
                    "name": course[1],
                    "description": course[2],
                    "months": course[3],
                    "fee": course[4]
                }
            )
# ---------------------------------------------------------
# Run this file directly
# ---------------------------------------------------------
if __name__ == "__main__":
    seed_courses()
    print(
        "Course data inserted successfully!"
    )