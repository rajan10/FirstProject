from state.chat_state import ChatState
from database.student_repository import find_student

# it accepts state which follows the ChatState structure and returns dict
def database_node(state:ChatState) -> dict:
    print("Executing database node")

    # state = { "question": "How much fee is due?","student_id": 101}
    student_id = state.get("student_id")

    if student_id is None:
        return {
            "context": (
                "Student ID was not provided. Payment information cannot be retrieved."
            )
        }

    student = find_student(student_id)
    if student is None:
        return {
            "context": (
                f"No student was found with student ID {student_id}."
            )
        }

    context = f"""
Student ID : {student['student_id']}
Student name: {student['name']}
Course: {student['course']}
Fee paid: INR {student['fee_paid']}
Fee due: INR {student['fee_due']}
Batch time: {student['batch_time']}
""".strip()

    return {"context": context}
"""
Now you have two protections:

student_id missing?
       │
       ├── YES → Friendly message
       │
       └── NO
            ↓
       Search database
            ↓
       Student found?
       │
       ├── NO → Friendly message
       │
       └── YES
            ↓
       Build context
"""