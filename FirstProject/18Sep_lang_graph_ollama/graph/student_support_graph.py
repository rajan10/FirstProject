# Build and connect the LangGraph workflow.
# This file tells LangGraph:
# Workflow orchestration which connects everything

# "When a question arrives, where should it go next?"
"""
# Think of ChatState as a backpack 🎒.

Every node can:
take something from the backpack
add something to the backpack
update something in the backpack

NODE = Worker 👷
ROUTER = Traffic Police 👮
GRAPH = Road Map 🗺️
"""

from langgraph.graph import END, START, StateGraph  # pyright: ignore[reportMissingImports]

from state.chat_state import ChatState
from nodes.classifier import classify_question
from nodes.database_node import database_node
from nodes.rag_node import rag_node
from nodes.api_node import api_node
from nodes.general_node import general_node
from nodes.answer_node import generate_answer
from graph.router import route_question


def build_graph():   
    # ChatState प्रयोग गर्ने workflow बनाऊ।"
    builder = StateGraph(ChatState) #  Create a LangGraph workflow whose state follows ChatState.
#  Create a graph node named "classify" and connect it to the Python function classify_question
#  key and actual node
    builder.add_node("classify", classify_question)  #which will return question
    builder.add_node("database", database_node)
    builder.add_node("rag", rag_node)
    builder.add_node("api", api_node)
    builder.add_node("general", general_node)
    builder.add_node("generate_answer", generate_answer)
    builder.add_edge(START, "classify") # every quesiton begins with  START -> CLASSIFIER  "कस्तो प्रश्न?"

    builder.add_conditional_edges(     # route_question returns database or rag or api or general # tells LangGraph HOW to follow that decision
        "classify",route_question,  # first classify then decides where to go like a traffic police as per route_question returns "कहाँ पठाउने?"
        {
            "database" : "database",
            "rag" : "rag",
            "api" : "api",
            "general" : "general",
        },
    )
#  after database node finishes or any other nodes finishes work, converge to single path called generate_answer
    builder.add_edge("database", "generate_answer")  #  connects each destination to the next step
    builder.add_edge("rag", "generate_answer")
    builder.add_edge("api", "generate_answer")
    builder.add_edge("general", "generate_answer")
    builder.add_edge("generate_answer", END)
    return builder.compile() # turns the blueprint into a runnable graph


graph = build_graph()
