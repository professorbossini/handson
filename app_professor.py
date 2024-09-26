#desafio 1
#O sistema deve dar uma mensagem de boas-vindas ao usuário.
#O sistema deve permitir que o usuário escolha o tipo de viagem que deseja: praia ou montanha.
#O sistema deve permitir que o usuário informe a quantia máxima que ele gostaria de gastar na viagem, ou seja, seu orçamento de viagem.
#Em função do orçamento informado, o sistema deve informar ao usuário que recomendará destinos econômicos, caso o orçamento seja menor do que R$3000. Caso contrário, o sistema deve informar que recomendará destinos premium.
#O sistema deve utilizar um serviço de IA para obter uma recomendação de viagem.
#O sistema deve utilizar um serviço de IA para gerar uma imagem que ilustra a recomendação que será entregue ao usuário.

import webbrowser
from dotenv import load_dotenv
from openai import OpenAI
load_dotenv()
client = OpenAI()

#desafio 2
print("Bem vindo ao sistema de recomendação de viagens")

#desafio 3
tipo_viagem = input("Escolha seu tipo de viagem: Praia ou montanha")

#desafio 4
orcamento = int(input("Quanto quer gastar?"))

#desafio 5
if orcamento < 3000:
    print('Vamos sugerir destinos econômicos')
else:
    print('Vamos sugerir destinos premium')


#desafio 6 montar o prompt para sugestâo
#se desejar, inclua uma localização, valor estimado para comer etc
prompt_sugestao = "Sugira uma viagem para a " + tipo_viagem + " restrita ao orcamento de " + str(orcamento)

completion = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=[
        {"role": "user", "content": f'{prompt_sugestao}. max:100 tokens'}
    ]
)


print(completion.choices[0].message.content)

#desafio 7 montar o prompt para imagem
#o que você quer ver? # Uma praia? Pessoas? Mochilas? Montanha? Um cachorro correndo atrás de uma bola? Seja criativo(a)!
prompt_imagem = "Uma foto de " + tipo_viagem + ". Pessoa viajando com orçamento restrito a " + str(orcamento)
response = client.images.generate(
    model="dall-e-3",
    prompt=prompt_imagem,
    n=1,
    size="1024x1024"
)

print(response.data[0].url)
webbrowser.open(response.data[0].url)