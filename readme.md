
# Descripción del consumo de la API de ChatGPT con Python

La API de ChatGPT es una herramienta de procesamiento de lenguaje natural (NLP) que utiliza la inteligencia artificial para generar respuestas automáticas a partir de una conversación.

En este documento se explicará cómo consumir la API de ChatGPT utilizando Python.


## Requisitos previos

Antes de comenzar a utilizar la API de ChatGPT, asegúrese de tener los siguientes requisitos previos instalados en su sistema:

- Python 3.x
- pip
- Una cuenta de OpenAI con acceso a la API de ChatGPT

## Instalación

Para instalar la librería de la API de OpenAI, ejecute el siguiente comando en la terminal:

```bash
  pip install openai
```

## Pasos

Para consumir la API de ChatGPT, primero debe obtener una clave API de OpenAI. Una vez que tenga su clave API, puede utilizar el siguiente código de ejemplo para conectarse a la API de ChatGPT y generar una respuesta automática a partir de una pregunta:

```bash
import openai

# Genera una API Key desde https://openai.com/api
openai.api_key = "OPENAI_API_KEY"


#bienvenida a mi app
print("Hola, soy Emma, tu asistente virtual.")
print("Estoy diseñada para apoyarte en tus reuniones")
print("Asi como para ayudarte a tomar decisiones importantes, y a resolver problemas de manera creativa.")


while True:

    prompt = input("\nEn que puedo ayudarte?: ")

    if prompt == "exit":
        break

    completion = openai.Completion.create(engine="text-davinci-003",
                                          prompt=prompt,
                                          max_tokens=2048)

    print(completion.choices[0].text)
    print("--------------------------------------------------------------------------------")
```

En este ejemplo, la variable prompt contiene la pregunta que se desea hacer a la API de ChatGPT. 

Con un if validamos si esta variable contiene la palabra exit, en el caso de que asi sea, detendremos el programa.

Luego, se utiliza el método openai.Completion.create() para enviar una solicitud a la API de ChatGPT donde se especifica el motor del modelo (engine="text-davinci-003"-> El mas actual hasta el momento), la consulta que realizamos contra la API de OpenAI (prompt), y la cantidad máxima de tokens (max_tokens).


El resultado de la solicitud se almacena en la variable completion, y la respuesta generada se imprime en la consola utilizando completion.choices[0].text. (el [0] indica que nos quedamos con el 1er valor de la respuesta)

Toda esta logica lo metemos dentro un bucle While con condición en true, para que se ejecute indfinidamente.


## Conclusiones
La API de ChatGPT es una poderosa herramienta para generar respuestas automáticas a partir de una conversación utilizando inteligencia artificial. Con Python, es fácil conectarse a la API de ChatGPT y utilizarla para generar respuestas a preguntas específicas. Sin embargo, es importante tener en cuenta que la calidad de las respuestas generadas dependerá en gran medida de la calidad de los datos utilizados para entrenar el modelo.


## Extras

Este programa y documentación fue extraida del siguiente video: https://www.youtube.com/watch?v=1Pl1FWHKHXQ&list=LL&index=2&t=242s&ab_channel=MoureDevbyBraisMoure





