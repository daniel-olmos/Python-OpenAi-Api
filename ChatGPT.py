import openai

# Tutorial en vídeo: https://youtu.be/1Pl1FWHKHXQ

# Genera una API Key desde https://openai.com/api
openai.api_key = "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"


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