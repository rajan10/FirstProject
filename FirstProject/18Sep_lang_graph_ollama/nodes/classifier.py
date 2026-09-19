from state.chat_state import ChatState

#ChatState भनेको chatbot ले एउटा node बाट अर्को node सम्म बोकेर हिँड्ने झोला 🎒 जस्तै हो।

def classify_question(state: ChatState) -> dict:  # state = {  "question": "How much is my course fee?" }
    question = state["question"].lower()

#"If the question contains one of these words, I will consider it a payment question."
    payment_words = [
        "fee",
        "payment",
        "paid",
        "pending amount",
        "due",
    ]
#"If the question contains one of these words, I will consider it a course question."
    course_words = [
        "course",
        "topics",
        "syllabus",
        "learn",
        "duration",
        "project",
    ]
#"If the question contains one of these words, I will consider it a api question."
    api_words = [
        "live",
        "api",
        "external",
        "service",
        "status",
    ]
#"If the question contains one of these words, I will consider it a payment question."
    if any(word in question for word in payment_words): # any() asks if at least ONE of these condition is true
        category = "payment"
    elif any(word in question for word in course_words):
        category = "course"
    elif any(word in question for word in api_words):
        category = "api"
    else:
        category = "general"

    print(f"Classifier Selected : {category}")

    return {
        "category": category
    }

"""
 👤 USER
                      │
                      ▼
             "What fee do I owe?"
                      │
                      ▼
             ┌─────────────────┐
             │   CLASSIFIER    │
             │                 │
             │ keyword check   │
             └────────┬────────┘
                      │
                      ▼
                  payment
                      │
                      ▼
             ┌─────────────────┐
             │ DATABASE NODE   │
             └────────┬────────┘
                      │
                 student_id
                      │
                      ▼
             ┌─────────────────┐
             │   REPOSITORY    │
             │                 │
             │ find_student()  │
             └────────┬────────┘
                      │
                      ▼
                students.db
                      │
                      ▼
             Student information
                      │
                      ▼
                  context
                      │
                      ▼
                    LLM
                      │
                      ▼
              👤 Final Answer
"""