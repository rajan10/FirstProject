from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Home Page"}

@app.get("/students/{student_id}")
def get_student(student_id: int):
    return {"student_id": student_id}

# Path parameters 
@app.get("/users/{username}")
def get_user(username: str):
    return {"username":username}

# Query parameter- question
@app.get("/search")
def search(name: str, age: int, course: str, fee: int):
    return {
        "name": name,
        "age": age,
        "course": course,   # ✅
        "fee": fee
    }