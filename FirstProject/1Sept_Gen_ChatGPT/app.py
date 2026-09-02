
import streamlit as st
from main import ask_gpt


# ============================================================
# PAGE CONFIGURATION
# ============================================================

st.set_page_config(
    page_title="AI Chatbot",
    page_icon="🤖",
    layout="wide",
    initial_sidebar_state="expanded"
)


# ============================================================
# CUSTOM CSS — CHATGPT-STYLE UI
# ============================================================

st.markdown("""
<style>

    /* ---------- GLOBAL ---------- */

    .stApp {
        background-color: #ffffff;
    }

    /* Remove default Streamlit top padding */
    .block-container {
        padding-top: 2rem;
        padding-bottom: 7rem;
        max-width: 900px;
    }


    /* ---------- SIDEBAR ---------- */

    [data-testid="stSidebar"] {
        background-color: #f7f7f8;
        border-right: 1px solid #e5e5e5;
    }

    [data-testid="stSidebar"] > div:first-child {
        padding-top: 1.5rem;
    }


    /* ---------- HEADER ---------- */

    .chat-header {
        text-align: center;
        padding: 10px 0 25px 0;
    }

    .chat-title {
        font-size: 30px;
        font-weight: 700;
        color: #202123;
        margin-bottom: 5px;
    }

    .chat-subtitle {
        font-size: 14px;
        color: #6b7280;
    }


    /* ---------- WELCOME SCREEN ---------- */

    .welcome-container {
        text-align: center;
        padding: 80px 20px 40px 20px;
    }

    .robot-icon {
        font-size: 55px;
        margin-bottom: 15px;
    }

    .welcome-title {
        font-size: 30px;
        font-weight: 700;
        color: #202123;
        margin-bottom: 10px;
    }

    .welcome-text {
        font-size: 16px;
        color: #6b7280;
        margin-bottom: 30px;
    }


    /* ---------- CHAT MESSAGES ---------- */

    .user-message {
        background-color: #f7f7f8;
        padding: 18px 20px;
        border-radius: 12px;
        margin: 12px 0;
        color: #202123;
        line-height: 1.6;
    }

    .assistant-message {
        background-color: #ffffff;
        padding: 18px 20px;
        border-radius: 12px;
        margin: 12px 0 25px 0;
        color: #202123;
        line-height: 1.7;
    }

    .message-label {
        font-weight: 700;
        font-size: 14px;
        margin-bottom: 8px;
    }


    /* ---------- CHAT INPUT ---------- */

    [data-testid="stChatInput"] {
        position: fixed;
        bottom: 20px;
        left: 50%;
        transform: translateX(-50%);
        width: min(850px, 90%);
        z-index: 999;
    }

    [data-testid="stChatInput"] textarea {
        border-radius: 18px !important;
        border: 1px solid #d9d9e3 !important;
        padding: 15px !important;
        font-size: 16px !important;
        background-color: #ffffff !important;
        box-shadow: 0 2px 10px rgba(0,0,0,0.08);
    }


    /* ---------- BUTTONS ---------- */

    .stButton button {
        border-radius: 8px;
        border: 1px solid #d9d9e3;
        background-color: #ffffff;
        color: #202123;
    }

    .stButton button:hover {
        border-color: #999999;
        background-color: #f7f7f8;
    }


    /* ---------- SIDEBAR BRAND ---------- */

    .brand {
        font-size: 21px;
        font-weight: 700;
        color: #202123;
        padding: 5px 0 20px 5px;
    }

    .brand span {
        font-size: 25px;
    }


    /* ---------- FOOTER ---------- */

    .footer {
        text-align: center;
        color: #9ca3af;
        font-size: 12px;
        margin-top: 30px;
    }

</style>
""", unsafe_allow_html=True)


# ============================================================
# SESSION STATE
# ============================================================

if "messages" not in st.session_state:
    st.session_state.messages = []


# ============================================================
# SIDEBAR
# ============================================================

with st.sidebar:

    st.markdown(
        '<div class="brand">🤖 AI Assistant</div>',
        unsafe_allow_html=True
    )

    st.divider()

    if st.button("➕ New Chat", use_container_width=True):
        st.session_state.messages = []
        st.rerun()

    st.markdown("### 💬 Chat")

    if st.session_state.messages:

        user_messages = [
            message["content"]
            for message in st.session_state.messages
            if message["role"] == "user"
        ]

        for i, message in enumerate(user_messages, 1):
            title = message[:30]

            if len(message) > 30:
                title += "..."

            st.caption(f"💬 {title}")

    st.divider()

    st.markdown("### ⚙️ About")

    st.caption(
        "Professional AI chatbot powered by GPT."
    )

    st.caption(
        "Ask questions, generate ideas, "
        "write code, or learn new topics."
    )


# ============================================================
# MAIN HEADER
# ============================================================

st.markdown("""
<div class="chat-header">

    <div class="chat-title">
        🤖 AI Assistant
    </div>

    <div class="chat-subtitle">
        Your intelligent AI-powered conversation partner
    </div>

</div>
""", unsafe_allow_html=True)


# ============================================================
# WELCOME SCREEN
# ============================================================

if not st.session_state.messages:

    st.markdown("""
    <div class="welcome-container">

        <div class="robot-icon">
            🤖
        </div>

        <div class="welcome-title">
            How can I help you today?
        </div>

        <div class="welcome-text">
            Ask me anything — coding, learning, writing,
            troubleshooting, ideas and more.
        </div>

    </div>
    """, unsafe_allow_html=True)


# ============================================================
# DISPLAY CHAT HISTORY
# ============================================================

for message in st.session_state.messages:

    if message["role"] == "user":

        st.markdown(
            f"""
            <div class="user-message">

                <div class="message-label">
                    👤 You
                </div>

                {message["content"]}

            </div>
            """,
            unsafe_allow_html=True
        )

    else:

        st.markdown(
            f"""
            <div class="assistant-message">

                <div class="message-label">
                    🤖 AI Assistant
                </div>

                {message["content"]}

            </div>
            """,
            unsafe_allow_html=True
        )


# ============================================================
# CHAT INPUT
# ============================================================

prompt = st.chat_input(
    "Message AI Assistant..."
)


# ============================================================
# PROCESS USER MESSAGE
# ============================================================

if prompt:

    # Store user message
    st.session_state.messages.append({
        "role": "user",
        "content": prompt
    })

    # Display user message immediately
    with st.chat_message("user", avatar="👤"):
        st.markdown(prompt)

    # Generate AI response
    with st.chat_message("assistant", avatar="🤖"):

        with st.spinner("Thinking..."):

            try:

                response = ask_gpt(prompt)

                if response is None:
                    response = "Sorry, I didn't receive a response."

                st.markdown(response)

                # Store AI response
                st.session_state.messages.append({
                    "role": "assistant",
                    "content": response
                })

            except Exception as e:

                error_message = (
                    "⚠️ **Something went wrong.**\n\n"
                    f"`{str(e)}`"
                )

                st.error(error_message)

                st.session_state.messages.append({
                    "role": "assistant",
                    "content": error_message
                })


# ============================================================
# FOOTER
# ============================================================

st.markdown(
    """
    <div class="footer">
        AI can make mistakes. Please verify important information.
    </div>
    """,
    unsafe_allow_html=True
)

