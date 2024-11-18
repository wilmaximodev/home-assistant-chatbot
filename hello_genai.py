import google.generativeai as genai
import os
import PyPDF2

genai.configure(api_key=os.environ["GEMINI_API_KEY"])

model = genai.GenerativeModel('gemini-1.5-flash')

with open('Wilcv.pdf', 'rb') as pdf_file:
    reader = PyPDF2.PdfReader(pdf_file)
    texto = ''
    
    for page in reader.pages:
        texto += page.extract_text()

response = model.generate_content(f'Aprimore meu curriculo com dicas pontuais, esse é o curriculo {texto}')

print(response.text)
