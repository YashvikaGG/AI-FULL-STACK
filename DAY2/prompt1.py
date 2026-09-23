import ollama
response=ollama.chat(
    model="llama3.2:3b",
    messages=[
        {
            "role":"user",
            "content": "Explain what is an AI in 6 linesp"
        }
    ]
)
print(response["message"]["content"])