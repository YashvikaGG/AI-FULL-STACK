import streamlit as st
import ollama

st.title("MY AI  ChatBot")
st.write("Welcome! Ask me anything.")
st.markdown("Hello **world**!")
uploaded_file = st.file_uploader("Choose a file")

if "messages" not in st.session_state:
    st.session_state.messages=[]

for message in st.session_state.messages:
    with  st.chat_message(message["role"]):
     st.write(message["content"])

question=st.chat_input("Type your message...")

if question:

    st.session_state.messages.append({
        "role":"user",
        "content":question
    })
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