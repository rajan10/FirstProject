from fastapi import FastAPI
app =FastAPI()

@app.get("/welcome")
def get_welcome_msg():
    return {"message": "welcome to FastAPI"}

@app.get("/greet")
def get_greet_mst():
    return{"message":"hello World"}