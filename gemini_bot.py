import os
import google.generativeai as genai

genai.configure(api_key="AIzaSyDxFB7XXvgLbZWW_YmD4crh6SnBPqWN5u4")

model = genai.GenerativeModel('gemini-pro')
chat = model.start_chat(history=[])

while True:
    prompt = input("Ask me anything: ")
    if (prompt == "exit"):
        break
    response = chat.send_message(prompt, stream=True)
    for chunk in response:
        if chunk.text:
          print(chunk.text)