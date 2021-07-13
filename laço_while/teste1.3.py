prompt = "\nA pratica leva a perfeição "
prompt += "\nTecle 's' para sair  "
prompt += "\nOu continue  "
prompt += "\nA escrever o que quiser  "
ativo = True
while ativo:
    message = input(prompt)
    if message == 's':
        ativo = False
    else:
        print(message)
