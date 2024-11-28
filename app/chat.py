import google.generativeai as genai
from google.api_core.exceptions import InvalidArgument
import os
import gradio as gr
import time

GEMINI_API_KEY = os.environ["GEMINI_API_KEY"]
genai.configure(api_key=GEMINI_API_KEY)

model = genai.GenerativeModel('gemini-1.5-flash')

chat = model.start_chat()
chat.send_message("Você é uma IA generativa capaz de processar texto e diversos tipos de arquivos. Sempre que alguém te fizer uma pergunta sobre um arquivo, verifique o histórico pra ver se algum arquivo foi enviado e bate com o pedido. Não diga que não é capaz de processar arquivos pois é!")

def gradio_wrapper(message, _history):
   uploaded_files = []

   for file_gradio_data in message["files"]:
        uploaded_file_info = genai.upload_file(file_gradio_data)
        while uploaded_file_info.state.name == "PROCESSING":
           time.sleep(3)
           uploaded_file_info = genai.get_file(uploaded_file_info.name)
        uploaded_files.append(uploaded_file_info)
   
   prompt = [message["text"]]
   prompt.extend(uploaded_files)
   
   try:
      response = chat.send_message(prompt)
   except InvalidArgument as e:
      response = chat.send_message(f"O usuario te usando, te enviou algum arquivo pra você ler e obteve um erro {e}. Por favor, peça pra ele tentar novamente e explique o que pode ter dado errado. A pessoa não entende de programação e não precisa ver o erro.")
      
   return response.text

chat_interface = gr.ChatInterface(
   fn=gradio_wrapper,
   title="Chatbot com Suporte a Arquivos 🤖",
   multimodal=True
)
chat_interface.launch()