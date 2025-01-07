import google.generativeai as genai
from google.api_core.exceptions import InvalidArgument
import os
import gradio as gr
import time
from home_assistant import set_light_values, intruder_alert, start_music, good_morning

GEMINI_API_KEY = os.environ["GEMINI_API_KEY"]
genai.configure(api_key=GEMINI_API_KEY)

model = genai.GenerativeModel(model_name='gemini-1.5-flash',
                              tools=[set_light_values, intruder_alert, start_music, good_morning])

chat = model.start_chat(enable_automatic_function_calling=True)
chat.send_message("Você é uma IA generativa capaz de processar texto e diversos tipos de arquivos. Sempre que alguém te fizer uma pergunta sobre um arquivo, verifique o histórico pra ver se algum arquivo foi enviado e bate com o pedido. Não diga que não é capaz de processar arquivos pois é!"
                  "Sempre em português"
                  "Você tem acesso a funções que podem ser chamadas automaticamente, como ajustar a luminosidade e a temperatura de cor das luzes, ativar o alerta de intruso, iniciar a reprodução de música e executar a rotina matinal"
                  "Você pode chamar essas funções automaticamente se achar que é o que o usuário deseja. Se não tiver certeza, pergunte ao usuário para confirmar se é isso que ele deseja"
                  "não exponha o código para o usuário, apenas o resultado da execução da função, se algo der errado, explique de forma simples e peça para o usuário tentar novamente")

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