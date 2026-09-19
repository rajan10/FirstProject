from typing import TypedDict


#Think of ChatState as the chatbot's backpack 🎒
class ChatState(TypedDict, total=False):
    question: str
    student_id: int
    category: str
    context: str
    answer: str


"""
state = {
    "question": "How much fee do I still owe?",
    "student_id": 101,
    "category": "payment"
}
"""