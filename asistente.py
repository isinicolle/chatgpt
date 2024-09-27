import openai

# Configura tu clave de API aquí
openai.api_key = 'TU_CLAVE_DE_API_AQUI'

def obtener_respuesta(pregunta):
    respuesta = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "user", "content": pregunta}
        ]
    )
    return respuesta['choices'][0]['message']['content']

if __name__ == "__main__":
    while True:
        pregunta = input("¿Cuál es tu pregunta? (Escribe 'salir' para terminar): ")
        if pregunta.lower() == 'salir':
            break
        respuesta = obtener_respuesta(pregunta)
        print("Asistente:", respuesta)
