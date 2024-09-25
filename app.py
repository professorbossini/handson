from openai import OpenAI
client = OpenAI()

#desafio 1
print("Bem vindo ao sistema de recomendação de viagens")

#desafio 2
tipo_viagem = input("Escolha seu tipo de viagem: Aventura ou relaxamento")

#desafio 3
orcamento = int(input("Quanto quer gastar?"))

#desafio 4
if orcamento < 3000:
    print('Vamos sugerir destinos econômicos')
else:
    print('Vamos sugerir destinos premium')


#desafio 5 montar o prompt
#se desejar, inclua uma localização
prompt_sugestao = "Sugira uma viagem em sao paulo do tipo " + tipo_viagem + " restrita ao orcamento de " + str(orcamento)

completion = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=[
        {"role": "user", "content": f'{prompt_sugestao}. max:100 tokens'}
    ]
)

#não mexa aqui ainda
print(completion.choices[0].message.content)