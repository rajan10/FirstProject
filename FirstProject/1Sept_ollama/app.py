import streamlit as st
from ollama_service import ask_ollama


# =====================================================
# PAGE SETTINGS
# =====================================================

st.set_page_config(
    page_title="Llama Chat",
    page_icon="🦙",
    layout="wide"
)


# =====================================================
# CUSTOM CSS
# =====================================================

st.markdown("""
<style>

    /* Main background */
    .stApp {
        background-color: #212121;
    }

    /* Sidebar */
    section[data-testid="stSidebar"] {
        background-color: #171717;
    }

    /* Main content width */
    .block-container {
        max-width: 900px;
        padding-top: 30px;
        padding-bottom: 120px;
    }

    /* Chat input */
    div[data-testid="stChatInput"] {
        background-color: #2f2f2f;
        border-radius: 15px;
    }

    /* Chat input text */
    div[data-testid="stChatInput"] textarea {
        color: white;
    }

</style>
""", unsafe_allow_html=True)


# =====================================================
# SESSION STATE
# =====================================================

if "messages" not in st.session_state:
    st.session_state.messages = []


# =====================================================
# SIDEBAR
# =====================================================

with st.sidebar:

    st.title("🦙 Llama Chat")

    st.caption("Local AI powered by Ollama")

    st.divider()

    if st.button(
        "➕ New Chat",
        use_container_width=True
    ):
        st.session_state.messages = []
        st.rerun()

    st.divider()

    st.subheader("Model")

    st.write("🦙 Llama 2")

    st.caption("Running locally through Ollama")

    st.divider()

    st.subheader("Privacy")

    st.caption(
        "🔒 Your conversation is processed "
        "through your local Ollama installation."
    )

    st.divider()

    if st.button(
        "🗑️ Clear Chat",
        use_container_width=True
    ):
        st.session_state.messages = []
        st.rerun()


# =====================================================
# MAIN HEADER
# =====================================================

st.title("🦙 Llama 2")

st.caption(
    "Your local AI assistant powered by Ollama"
)


# =====================================================
# WELCOME SCREEN
# =====================================================

if len(st.session_state.messages) == 0:

    st.info(
        "👋 Welcome! Ask me anything to get started."
    )


# =====================================================
# DISPLAY PREVIOUS MESSAGES
# =====================================================

for message in st.session_state.messages:

    if message["role"] == "user":

        with st.chat_message(
            "user",
            avatar="👤"
        ):
            st.markdown(message["content"])

    else:

        with st.chat_message(
            "assistant",
            avatar="🦙"
        ):
            st.markdown(message["content"])


# =====================================================
# CHAT INPUT
# =====================================================

user_input = st.chat_input(
    "Message Llama..."
)


# =====================================================
# SEND MESSAGE
# =====================================================

if user_input:

    # Save user message
    st.session_state.messages.append(
        {
            "role": "user",
            "content": user_input
        }
    )

    # Display user message
    with st.chat_message(
        "user",
        avatar="👤"
    ):
        st.markdown(user_input)


    # Get AI response
    with st.chat_message(
        "assistant",
        avatar="🦙"
    ):

        with st.spinner("Llama is thinking..."):

            try:

                answer = ask_ollama(
                    st.session_state.messages
                )

                st.markdown(answer)

            except Exception as e:

                answer = (
                    "⚠️ I couldn't connect to Ollama.\n\n"
                    "Please make sure Ollama is running "
                    "and that the `llama2` model is installed."
                )

                st.error(answer)

                # Show technical error in terminal,
                # not in the chat UI
                print("Ollama error:", e)


    # Save assistant response
    st.session_state.messages.append(
        {
            "role": "assistant",
            "content": answer
        }
    )