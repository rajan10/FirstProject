# Agent represents AI worker and has Role, goal, backstory and LLM
from crewai import (
    Agent,
    Task,
    Crew,
    Process,
    LLM,
)  # Crew combines agents and tasks (agents+tasks+process = crew) crew =AI Team
from dotenv import load_dotenv
import os

# ============================================================
# LOAD LOCAL CONFIGURATION
# ============================================================
# load to Python  and os.getenv to interact with env var and os functionality
load_dotenv()  # read the .env file so now Python knows all Constants in the .env

OLLAMA_MODEL = os.getenv(
    "OLLAMA_MODEL", "llama3.2:3b"
)  # if .env contains OLLAMA_MODEL use it else use llama3.2:3b
OLLAMA_BASE_URL = os.getenv(
    "OLLAMA_BASE_URL", "http://localhost:11434"
)  # where is ollama
OLLAMA_TEMPERATURE = float(
    os.getenv("OLLAMA_TEMPERATURE", "0.2")
)  # as .env variables are normally read as strings we convert
OLLAMA_TIMEOUT = int(os.getenv("OLLAMA_TIMEOUT", "180"))


# ============================================================
# CREATE OLLAMA LLM
# ============================================================
def get_ollama_llm():
    # Get/ create Ollama AI model to be handed to CrewAI
    return LLM(
        model=f"ollama/{OLLAMA_MODEL}",  # Ollama provider/ Ollama model name
        base_url=OLLAMA_BASE_URL,
        temperature=OLLAMA_TEMPERATURE,
        timeout=OLLAMA_TIMEOUT,
    )


# ============================================================
# GENERATE COURSE CONTENT
# ============================================================


def generate_course_content(course_name: str):
    """
    Run a two-agent CrewAI workflow:

    Researcher Agent
        ↓
    Research Task
        ↓
    Writer Agent
        ↓
    Final Course Content
    """

    if not course_name or not course_name.strip():
        raise ValueError("Course name cannot be empty.")

    llm = get_ollama_llm()

    # --------------------------------------------------------
    # AGENT 1: COURSE RESEARCHER
    # --------------------------------------------------------
    research_agent = Agent(
        role="Course Researcher",  # who am I?
        goal=(  # what do you want me to accomplish?
            "Research the given course and identify important topics, "
            "student skills, practical projects, and learning outcomes."
        ),
        backstory=(  # personality/context
            "You are an experienced technical course researcher. "
            "You understand how to break complex technical subjects "
            "into practical learning paths for students."
        ),
        llm=llm,  # llm gives AI brain to agent. As Agent + LLM  = AI Worker
        verbose=True,  # provide detail execution info useful for learning/debugging
        allow_delegation=False,  # do your task and not delegat to another agent
        max_iter=5,  # how many times the agent can perform during execution.  एकै काममा endlessly नघुम just 5 times think
    )

    # --------------------------------------------------------
    # AGENT 2: COURSE CONTENT WRITER
    # --------------------------------------------------------

    writer_agent = Agent(
        role="Course Content Writer",
        goal=(
            "Create simple, clear, accurate, and student-friendly "
            "course content based on the research provided."
        ),
        backstory=(
            "You are an experienced educational content writer. "
            "You explain technical subjects in simple English and "
            "organize information so beginners can understand it."
        ),
        llm=llm,
        verbose=True,
        allow_delegation=False,
        max_iter=5,
    )

    # --------------------------------------------------------
    # TASK 1: RESEARCH
    # --------------------------------------------------------

    research_task = Task(
        description=f"""
Research the course: {course_name}

Identify: 

1. Important topics students should learn
2. Core technical concepts
3. Skills students will gain
4. Practical project ideas
5. Suggested beginner-to-intermediate learning progression

Keep the research practical and student-friendly.

Return a structured research report with clear headings.
""",
        expected_output="""
A structured research report containing:

- Important Topics
- Core Concepts
- Student Skills
- Practical Project Ideas
- Suggested Learning Progression
""",
        agent=research_agent,
    )

    # --------------------------------------------------------
    # TASK 2: WRITING
    # --------------------------------------------------------

    writing_task = Task(
        description=f"""
Create complete course content for:

{course_name}

Use the research produced by the Course Researcher.

Prepare the following sections:

1. COURSE INTRODUCTION
   - What is the course?
   - Why should students learn it?
   - Where is it used?

2. COURSE HIGHLIGHTS
   - Important topics
   - Core concepts
   - Student skills
   - Practical projects

3. IMPORTANT TOPICS
   - Organize topics logically from beginner to advanced.

4. SKILLS STUDENTS WILL LEARN
   - Technical skills
   - Practical skills

5. PROJECT IDEAS
   - Give realistic projects.
   - Explain briefly what each project teaches.

6. LEARNING OUTCOMES
   - Explain what students should be able to do after completing
     the course.

7. FINAL STUDENT-FRIENDLY SUMMARY
   - Give a simple summary of the complete course.

Rules:
- Use simple English.
- Do not invent certifications, statistics, or guaranteed job outcomes.
- Do not mention that you are an AI.
- Make the content useful for students.
""",
        expected_output="""
A complete student-friendly course document containing:

COURSE INTRODUCTION

COURSE HIGHLIGHTS

IMPORTANT TOPICS

SKILLS STUDENTS WILL LEARN

PROJECT IDEAS

LEARNING OUTCOMES

FINAL STUDENT-FRIENDLY SUMMARY
""",
        agent=writer_agent,
        context=[
            research_task
        ],  # Writer use the output of the Research Task as context.
    )

    # --------------------------------------------------------
    # CREATE CREWS  RSEARCHER & WRITER
    # --------------------------------------------------------

    crew = Crew(  # create crew object that contains  Researcher and the writer
        agents=[research_agent, writer_agent],
        tasks=[research_task, writing_task],
        process=Process.sequential,  # process must be one after another in sequential order
        verbose=True,  # show execution details
    )

    # --------------------------------------------------------
    # EXECUTE MULTI-AGENT WORKFLOW
    # --------------------------------------------------------

    result = crew.kickoff()

    return result
