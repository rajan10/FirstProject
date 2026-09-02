from fastapi import FastAPI, HTTPException
from courses import course
from pydantic import BaseModel
ap =FastAPI()
@ap.get("/courses/{course_id}")
def get_course(course_id: int):
    if course is None:
        raise HTTPException(
            status_code=404,
            detail="Course not found"
        )
    return course[course_id]
class Course(BaseModel):
    course_id: int
    name:str
    instructor: str
    fee:int
@ap.get("/courses/courses-all/")
def get_course_all():
    return {"message":"course retrieved",
            "course":course}
@ap.put("/courses/{course_id}/{instructor}",status_code=200)
def course_update(course_id: int, instructor: str):
    result=get_course(course_id)
    result['instructor']=instructor
    return {"message":"record updated successfully!",
            "course":course}
@ap.post("/courses/", status_code=201)
def course_create(new_course: Course):
    new_id=len(course)+1
    course[new_id]={"name":new_course.name,
                    "instructor":new_course.instructor,
                    "fee":new_course.fee
    }
    # create a dict from the pydantic model and add Phone
    updated_new_course = new_course.model_dump()
    updated_new_course["Phone"] = 9843035921
    return {
        "message": "Course created successfully!",
        "course": updated_new_course
    }
@ap.patch("/courses/{course_id}")
def course_partial_update(course_id: int, update_course: Course): # what ever the client (swagger) sends the request comes here

    existing_course = course.get(course_id) # you cud have used course[3] as it is a pydantic model(python object) but with get() it is safe 

    if existing_course is None:
        raise HTTPException(
            status_code=404,
            detail="Course not found"
        )

    update_data = update_course.model_dump(exclude_unset=True) # first converts to dictionary and with exclude_unset=true only that changed attribute

    existing_course.update(update_data) #Python dictionary has update() method

    return {
        "message": "Course updated successfully",
        "course": existing_course #fastAPI automatically converts this dictionary into JSON
    }
    
    
    

