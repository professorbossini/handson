#desafio 1
#Escreva aqui seu primeiro requisito
#Escreva aqui seu segundo requisito
#Escreva aqui seu terceiro requisito

import webbrowser
from dotenv import load_dotenv
from openai import OpenAI
load_dotenv()
client = OpenAI()

#desafio 2 - Exibir mensagem de boas vindas


#desafio 3 - Permitir que o usuário informe o tipo de viagem desejado e guardar em uma variável


#desafio 4 - Permitir que o usuário informe seu orçamento e guardar a sua representação numérica em uma variável


#desafio 5 - Em função do orçamento informado pelo usuário, dizer a ele se a recomendação será econômica ou premium



#desafio 6 montar o prompt para sugestâo
#se desejar, inclua uma localização, valor estimado para comer etc
# prompt_sugestao = ""

# completion = client.chat.completions.create(
#     model="gpt-4o-mini",
#     messages=[
#         {"role": "user", "content": f'{prompt_sugestao}. max:100 tokens'}
#     ]
# )


#Remova esse comentário quando o professor pedir, ok? :)
#print(completion.choices[0].message.content)

#desafio 7 montar o prompt para imagem
#o que você quer ver? # Uma praia? Pessoas? Mochilas? Montanha? Um cachorro correndo atrás de uma bola? Seja criativo(a)!
# prompt_imagem = ""
# response = client.images.generate(
#     model="dall-e-3",
#     prompt=prompt_imagem,
#     n=1,
#     size="1024x1024"
# )

#Remova esse comentário quando o professor pedir, ok? :)
#webbrowser.open(response.data[0].url)