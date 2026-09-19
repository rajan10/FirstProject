from state.chat_state import ChatState

def route_question(state: ChatState):

    """ if 
    state = {
    "question": "What is my fee?",
    "category": "payment",
    "student_id": 101  THEN  state["category"] = payment
}
    """

    category = state["category"]

    if category == "payment":
        return "database"

    elif category == "course":
        return "rag"

    elif category == "live":
        return "api"

    else:
        return "general"