import streamlit as st
import ollama

st.title("MY AI  ChatBot")
st.write("Welcome! Ask me anything.")
st.markdown("Hello **world**!")

if "messages" not in st.session_state:
    st.session_state.messages=[]

for message in st.session_state.messages:
    with  st.chat_message(message["role"]):
     st.write(message["content"])

question = st.chat_input(
    "Type your message...",
    accept_file=True,
    file_type=["pdf", "txt", "docx"]
)

uploaded_file = None

if question:
    uploaded_file = question["files"][0] if question["files"] else None
    question_text = question["text"]

if question:

    st.session_state.messages.append({
        "role":"user",
        "content":question
    })
if uploaded_file:
    st.write("File:", uploaded_file.name)
    with st.chat_message("user"):
        st.write(question)
    response=ollama.chat(
        model="llama3.2:3b",
        messages=st.session_state.messages
    )
    answer=response["message"]["content"]
    st.session_state.messages.append({
        "role":"assitant",
        "content":answer
    })
    with st.chat_message("assistant"):
        st.write(answer)