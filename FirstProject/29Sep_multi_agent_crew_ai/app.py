import streamlit as st
from main import (
    generate_course_content,
    OLLAMA_MODEL,
    OLLAMA_BASE_URL,
)

# ============================================================
# PAGE CONFIG
# ============================================================

st.set_page_config(
    page_title="AI Course Content Generator",
    page_icon="🎓",
    layout="wide",
)


# ============================================================
# CUSTOM CSS
# ============================================================

st.markdown(
    """
    <style>
    .main-title {
        font-size: 42px;
        font-weight: 700;
        text-align: center;
        margin-bottom: 5px;
    }

    .subtitle {
        text-align: center;
        color: #666;
        font-size: 18px;
        margin-bottom: 35px;
    }

    .course-card {
        padding: 25px;
        border-radius: 15px;
        background-color: #f8f9fa;
        border: 1px solid #e5e7eb;
        margin-bottom: 20px;
    }

    .local-badge {
        text-align: center;
        padding: 8px;
        border-radius: 10px;
        background-color: #eef6ff;
        margin-bottom: 20px;
    }
    </style>
    """,
    unsafe_allow_html=True,
)


# ============================================================
# HEADER
# ============================================================

st.markdown(
    '<div class="main-title">🎓 AI Course Content Generator</div>',
    unsafe_allow_html=True,
)

st.markdown(
    '<div class="subtitle">'
    "CrewAI Multi-Agent System powered by local Ollama"
    "</div>",
    unsafe_allow_html=True,
)

st.markdown(
    f"""
    <div class="local-badge">
        🟢 <strong>Local AI</strong> |
        Model: <strong>{OLLAMA_MODEL}</strong> |
        Ollama: <strong>{OLLAMA_BASE_URL}</strong>
    </div>
    """,
    unsafe_allow_html=True,
)


# ============================================================
# SIDEBAR
# ============================================================

with st.sidebar:
    st.header("⚙️ Configuration")

    st.write("**LLM Provider:** Ollama")
    st.write(f"**Model:** `{OLLAMA_MODEL}`")
    st.write(f"**URL:** `{OLLAMA_BASE_URL}`")

    st.divider()

    st.markdown("""
        ### 🤖 Agent Team

        **1. Course Researcher 🔍**
        - Researches topics
        - Identifies skills
        - Suggests projects

        **2. Course Writer ✍️**
        - Uses research
        - Creates course content
        - Produces student-friendly output
        """)


# ============================================================
# INPUT
# ============================================================

st.markdown("### 📚 Course Details")

course_name = st.text_input(
    "Enter Course Name",
    placeholder="Example: Generative AI and Agentic AI",
)


# ============================================================
# GENERATE
# ============================================================

generate_button = st.button(
    "🚀 Generate Course Content",
    use_container_width=True,
)


if generate_button:

    if not course_name.strip():
        st.warning("⚠️ Please enter a course name.")

    else:

        with st.spinner("🤖 Researcher Agent → Writer Agent → Final Course..."):

            try:
                result = generate_course_content(course_name)

                st.success("✅ Course content generated successfully!")

                # ---------------------------------------------
                # RESULT
                # ---------------------------------------------

                st.markdown("## 📄 Generated Course Content")

                st.markdown(
                    '<div class="course-card">',
                    unsafe_allow_html=True,
                )

                st.markdown(str(result))

                st.markdown(
                    "</div>",
                    unsafe_allow_html=True,
                )

                # ---------------------------------------------
                # DOWNLOAD
                # ---------------------------------------------

                st.download_button(
                    label="⬇️ Download Course Content",
                    data=str(result),
                    file_name=(f"{course_name.strip()}_course_content.txt"),
                    mime="text/plain",
                    use_container_width=True,
                )

            except Exception as e:

                st.error("❌ Error while generating content.")

                with st.expander("🔎 Show technical error"):
                    st.exception(e)
