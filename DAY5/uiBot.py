import ollama
import streamlit as st

st.title("Welcome to ChatBot App!!")
with st.sidebar:
    uploaded_file=st.file_uploader("Upload a text file...")
    if uploaded_file:
        st.write("File uploaded successfully")
        context = uploaded_file.read().decode("utf-8")
        st.write("file content:",context
           if context
           else "No content to display")


# Store conversation history
if "msgs" not in st.session_state:
    st.session_state.msgs = []

# Display previous messages
for msg in st.session_state.msgs:
    with st.chat_message(msg["role"]):
        st.write(msg["content"])

# Chat input
question = st.chat_input("You:")

if question:
    st.session_state.msgs.append({
        "role": "user",
        "content": question
    })
    with st.chat_message("user"):
        st.write(question)
    with st.spinner("Thinking..."):
        response = ollama.chat(
            model="llama3.2:3b",
            messages=st.session_state.msgs
        )
    answer = response["message"]["content"]
    st.session_state.msgs.append({
        "role": "assistant",
        "content": answer
    })
    with st.chat_message("assistant"):
        st.write(answer)