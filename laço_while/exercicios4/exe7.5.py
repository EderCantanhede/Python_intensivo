"""
7.5 – Ingressos para o cinema: Um cinema cobra preços diferentes para os
ingressos de acordo com a idade de uma pessoa. Se uma pessoa tiver menos
de 3 anos de idade, o ingresso será gratuito; se tiver entre 3 e 12 anos, o
ingresso custará 10 dólares; se tiver mais de 12 anos, o ingresso custará 15
dólares. Escreva um laço em que você pergunte a idade aos usuários e, então,
informe-lhes o preço do ingresso do cinema.
"""
idade = int(input("Informe a sua idade? "))

while idade != 'quit':
    break
if idade <= 3:
    print("Seu ingresso é gratuito! ")
else:
    print("Seu ingresso é dez dólares")
