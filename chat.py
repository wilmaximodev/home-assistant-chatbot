import google.generativeai as genai
import os
import gradio as gr

genai.configure(api_key=os.environ["GEMINI_API_KEY"])
model = genai.GenerativeModel('gemini-1.5-flash')

chat = model.start_chat()

def gradio_wrapper(message, _history):
    response = chat.send_message(message)
    return response.text

chatInterface = gr.ChatInterface(gradio_wrapper)
chatInterface.launch()