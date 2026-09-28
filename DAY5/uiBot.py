import ollama
import streamlit as st

st.title("Welcome to ChatBot App!!")
st.markdown(":red[***HELLO***]")
with st.sidebar:
    st.header("chat settings")
    if st.button("clear chat 🗑️ "):
        st.session_state.msgs=[]
        st.success("Chat Cleared")
    personalities={
        "Kid":"Answer the questions like you are explaining to a 5 year old kid.Give answers in 2 lines only",
        "Friend":"Answer the questions friendly and casual manner.Give answers in 2 lines only",
        "English Tutor":"Teach english like an english scholar.and reply with only 2 lines of answers only"
    }
    personality=st.selectbox("select a  personaliy",personalities.keys())
    uploaded_file=st.file_uploader("Upload a text file...")
    try:
        if uploaded_file:
             st.write("File uploaded successfully")
             content = uploaded_file.read().decode("utf-8")
             if st.button("Display"):
                  st.text(content)
    except:
        st.error("Can't read this file.")

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
            messages=[{
    "role":"system",
    "content":"personalities[personality]"
}]+st.session_state.msgs
        )
    answer = response["message"]["content"]
    st.session_state.msgs.append({
        "role": "assistant",
        "content": answer
    })
    with st.chat_message("assistant"):
        st.write(answer)