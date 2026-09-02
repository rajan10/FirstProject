import streamlit as st
import os

# ----------------------------
# Page Configuration
# ----------------------------
st.set_page_config(
    page_title="Student Registration",
    page_icon="🎓",
    layout="wide"
)

# ----------------------------
# Sidebar
# ----------------------------
st.sidebar.title("📚 Navigation")
st.sidebar.write("Welcome to the Student Registration Portal")
st.sidebar.info(
    """
    **Courses Available**
    - Java
    - Python
    - Agentic AI
    """
)

# ----------------------------
# Title Section
# ----------------------------
st.title("🎓 Student Registration Portal")
st.markdown("### Register for your favourite technology course")
st.divider()

# ----------------------------
# Form
# ----------------------------
with st.form("registration_form"):

    col1, col2 = st.columns(2)

    with col1:
        name = st.text_input("👤 Full Name")

    with col2:
        email = st.text_input("📧 Email Address")

    course = st.selectbox(
        "📖 Select Course",
        ["Java", "Python", "Agentic AI"]
    )

    uploaded_file = st.file_uploader(
        "📄 Upload Resume",
        type=["pdf", "doc", "docx"]
    )

    submit = st.form_submit_button("🚀 Register")

# ----------------------------
# Submit
# ----------------------------
if submit:

    if not name or not email:
        st.error("Please enter both Name and Email.")
    else:

        st.success("Registration Successful 🎉")

        st.subheader("Registration Details")

        st.write("**Name:**", name)
        st.write("**Email:**", email)
        st.write("**Course:**", course)

        if uploaded_file is not None:

            upload_folder = "uploads"
            os.makedirs(upload_folder, exist_ok=True)

            filepath = os.path.join(upload_folder, uploaded_file.name)

            with open(filepath, "wb") as file:
                file.write(uploaded_file.getbuffer())

            st.success("Resume uploaded successfully.")

            st.subheader("Uploaded File Information")

            col1, col2, col3 = st.columns(3)

            with col1:
                st.metric("File Name", uploaded_file.name)

            with col2:
                st.metric(
                    "File Size",
                    f"{uploaded_file.size/1024:.2f} KB"
                )

            with col3:
                st.metric(
                    "File Type",
                    uploaded_file.type
                )

        else:
            st.warning("No resume uploaded.")

st.divider()

st.info(f"📂 Current Working Directory\n\n{os.getcwd()}")