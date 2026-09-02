from pydantic import BaseModel
from fastapi import FastAPI

app = FastAPI()
class Student(BaseModel):
    name: str
    age: int

@app.post("/students")
def create_student(student: Student):
    return {"Student Name":student.name,
            "Student Age": student.age}