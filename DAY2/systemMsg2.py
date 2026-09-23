import ollama
response=ollama.chat(
    model="llama3.2:3b",
    messages=[
        {
            "role":"system",
            "content":"Give answers in 2 lines only as if you are explaining a 5 year old kid."
        },
        {
            "role":"user",
            "content": "Explain AI"
        }
    ]
)
print(response["message"]["content"])