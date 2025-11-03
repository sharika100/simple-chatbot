# app.py
import streamlit as st
from chatbot import get_response

st.set_page_config(page_title="Simple Chatbot 🤖", layout="centered")
st.title("💬 Simple Chatbot")

if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

user_input = st.text_input("You:", "")

if st.button("Send") and user_input:
    response = get_response(user_input)
    st.session_state.chat_history.append(("You", user_input))
    st.session_state.chat_history.append(("Bot", response))

for speaker, message in st.session_state.chat_history:
    if speaker == "You":
        st.markdown(f"**🧑‍💻 {speaker}:** {message}")
    else:
        st.markdown(f"**🤖 {speaker}:** {message}")
