---

# 🔥 Assistente Virtual para Casa Inteligente  

Um chatbot baseado em **IA generativa** que pode processar texto e arquivos, além de **chamar funções automaticamente** para controlar dispositivos domésticos inteligentes.  

## 🌟 Funcionalidades  
- **Controle de iluminação** – Ajuste de brilho e temperatura de cor  
- **Alerta de intruso** – Acionamento automático do sistema de segurança  
- **Música ambiente** – Reprodução de música sob demanda  
- **Rotina matinal** – Configuração de ambiente e tarefas diárias  
- **Processamento de arquivos** – Envio e análise de documentos  
- **Conversação inteligente** – O assistente entende comandos e pode chamar funções automaticamente  

## 🚀 Tecnologias  
- **Python**  
- **Google Gemini AI** (IA generativa com suporte a chamadas de função)  
- **Gradio** (Interface interativa para chatbot)  

## 📦 Instalação  

### 1️⃣ Clone o repositório  
```sh
git clone https://github.com/seu-usuario/home-assistant-chatbot.git
cd home-assistant-chatbot
```

### 2️⃣ Crie um ambiente virtual e ative  
```sh
python3 -m venv .venv
source .venv/bin/activate  # No Windows: .venv\Scripts\activate
```

### 3️⃣ Instale as dependências  
```sh
pip install -r requirements.txt
```

### 4️⃣ Configure a chave da API Gemini  
Crie um arquivo **`.env`** na raiz do projeto e adicione sua chave da API do Google Gemini:  
```
GEMINI_API_KEY=your_api_key_here
```

---

## ▶️ Como Usar  
Inicie o chatbot com o seguinte comando:  
```sh
python app.py
```
A interface será aberta no navegador, permitindo que você interaja com o assistente.  

---

## 📝 Estrutura do Projeto  
```
home-assistant-chatbot/
│── home_assistant/
│   ├── set_light_values.py    # Função para ajuste de iluminação
│   ├── intruder_alert.py      # Função para alerta de intruso
│   ├── start_music.py         # Função para iniciar reprodução de música
│   ├── good_morning.py        # Função para rotina matinal
│── app.py                     # Código principal do chatbot
│── requirements.txt            # Dependências do projeto
│── README.md                   # Documentação do projeto
```

---

## 🏡 Sobre o Projeto  
Esse assistente foi projetado para facilitar a automação residencial com **IA generativa e chamadas de função inteligentes**. Ele entende comandos e **executa ações automaticamente** sempre que necessário.  

Se quiser testar ou contribuir, fique à vontade!  

#IA #Chatbot #SmartHome #Automação #Python #GeminiAI #Gradio  

---
