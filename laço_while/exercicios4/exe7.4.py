"""
7.4 – Ingredientes para uma pizza: Escreva um laço que peça ao usuário para
fornecer uma série de ingredientes para uma pizza até que o valor 'quit' seja
fornecido. À medida que cada ingrediente é especificado, apresente uma
mensagem informando que você acrescentará esse ingrediente à pizza.
"""

prompt = "\nInforme quais ingredientes você deseja acrescentar em seu podido? "
prompt += "\nAssim que concluir por favor tecle 'quit'! "

while True:
    pizza = input(prompt)
    if pizza == 'quit':
        break
    else:
        print("Seu pedido ficara pronto em 5 minutos ")
        print("E esses ingredientes: " + pizza.title() + " serão acrescentados ao seu pedido")
