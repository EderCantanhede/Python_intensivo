usuarios_atuais = ['Pedro', 'Paulo', 'Ilana', 'Zoe', 'Carla', 'Beatriz']
novos_usuarios = ['Heitor', 'Josué', 'Calebe', 'Raíssa', 'zoe', 'Beatriz']
for x in novos_usuarios:
    if x in usuarios_atuais:
        print("Nome de usuário não disponível!")

novo_nome = str(input("Forneça um novo nome:"))

if novo_nome in usuarios_atuais:
    print("Nome de usuário não disponível!")
else:
    print("Nome de usuário disponível")
    usuarios_atuais.append(novo_nome)
print(usuarios_atuais)
