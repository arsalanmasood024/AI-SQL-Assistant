import streamlit as st


def init_chat():

    if "messages" not in st.session_state:
        st.session_state.messages = []


def add_user_message(text):

    st.session_state.messages.append(
        {
            "role": "user",
            "content": text
        }
    )


def add_ai_message(text):

    st.session_state.messages.append(
        {
            "role": "assistant",
            "content": text
        }
    )


def show_chat():

    for message in st.session_state.messages:

        with st.chat_message(message["role"]):

            st.markdown(message["content"])


def clear_chat():

    st.session_state.messages = []