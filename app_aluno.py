#desafio 1
#escreva seu primeiro requisito
#escreva seu segundo requisito
#escreva seu terceiro requisito
import webbrowser
from openai import OpenAI
client = OpenAI()

#desafio 2 - exibir mensagem de boas vindas


#desafio 3 - capturar o tipo de viagem que o usuário deseja: montanha ou praia


#desafio 4 - capturar o orçamento do usuário, representação numérica


#desafio 5 - decidir se a sugestâo é para viagem econômica ou premium e mostrar para o usuário

#desafio 6 - montar o prompt para pedir ao chatgpt a sugestão de viagem
#se desejar, inclua uma localização, valor estimado para comer etc
prompt_sugestao = None

completion = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=[
        {"role": "user", "content": f'{prompt_sugestao}. max:100 tokens'}
    ]
)

#remova este comentário quando o professor falar, ok?:)
#print(completion.choices[0].message.content)

#desafio 7 - montar o prompt para pedir ao chatgpt a imagem
#o que você quer ver? 
# Uma praia? Pessoas? Mochilas? Montanha? Um cachorro correndo atrás de uma bola?Seja criativo(a)!
prompt_imagem = None
response = client.images.generate(
    model="dall-e-3",
    prompt=prompt_imagem,
    n=1,
    size="1024x1024"
)

print(response.data[0].url)
webbrowser.open(response.data[0].url)