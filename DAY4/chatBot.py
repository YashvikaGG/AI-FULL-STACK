import ollama
msgs=[{
     "role":"system",
     "content":"You are an esteemed professor in an IIT,give answers as if you are helping out of a first year student"
}]
while True:
    question = input("YOU: ")
    if question.lower()=="exit":
         break
    msgs.append(
         {"role":"user",
          "content": question }
    )
    response=ollama.chat(
        model="llama3.2:3b",
        messages=msgs   )
    msgs.append(
         {
              
              "role":"assistant",
              "content":response["message"]["content"]
         }
    )
    print("AI:",response["message"]["content"])
print("-----CHAT HISTORY-----\n")
for msg in msgs:
     print(msg["role"],":",msg["content"])
    