import ollama
response=ollama.chat(
    model="llama3.2:3b",
    messages=[
        {
            "role":"user",
            "content": "Give the definition of AI and Give only the names of 3 main types of AI and Give 3 examples of AI and explain one line description about each example in bullet points only"
        }
    ]
)
print(response["message"]["content"])