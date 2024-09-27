import openai
import os
import tkinter as tk
from tkinter import scrolledtext
from dotenv import load_dotenv

# Cargar las variables de entorno desde el archivo .env
load_dotenv()
openai.api_key = os.getenv('OPENAI_API_KEY')

def obtener_respuesta(pregunta):
    try:
        respuesta = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": pregunta}]
        )
        return respuesta['choices'][0]['message']['content']
    except Exception as e:
        print("Error:", e)
        return "Error en la API."

def enviar_pregunta():
    pregunta = entry_pregunta.get()
    if pregunta:
        respuesta = obtener_respuesta(pregunta)
        text_area.insert(tk.END, f"Tú: {pregunta}\n")
        text_area.insert(tk.END, f"Asistente: {respuesta}\n\n")
        entry_pregunta.delete(0, tk.END)

# Configuración de la ventana
root = tk.Tk()
root.title("Asistente Virtual")

# Cuadro de entrada
entry_pregunta = tk.Entry(root, width=50)
entry_pregunta.pack(pady=10)

# Botón para enviar pregunta
btn_enviar = tk.Button(root, text="Enviar", command=enviar_pregunta)
btn_enviar.pack(pady=5)

# Área de texto para mostrar la conversación
text_area = scrolledtext.ScrolledText(root, width=60, height=20)
text_area.pack(pady=10)

# Ejecutar la aplicación
root.mainloop()
