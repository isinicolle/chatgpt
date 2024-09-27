import openai
import os
from dotenv import load_dotenv

# Cargar las variables de entorno desde el archivo .env
load_dotenv()

# Obtener la clave de API de la variable de entorno
openai.api_key = os.getenv('OPENAI_API_KEY')

def obtener_respuesta(pregunta):
    try:
        respuesta = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "user", "content": pregunta}
            ]
        )
        return respuesta['choices'][0]['message']['content']
    except Exception as e:
        print("Error:", e)
        return None

if __name__ == "__main__":
    while True:
        pregunta = input("¿Cuál es tu pregunta? (Escribe 'salir' para terminar): ")
        if pregunta.lower() == 'salir':
            break
        respuesta = obtener_respuesta(pregunta)
        if respuesta:  # Verifica si se obtuvo una respuesta
            print("Asistente:", respuesta)
        else:
            print("No se pudo obtener una respuesta.")