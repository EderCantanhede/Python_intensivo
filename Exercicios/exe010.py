lista_de_convidados = ["José", "Maria", "Simone", "Vanilson"]
mensagem = "Estarei realizando um jantar em minha casa " \
           "e gostaria de contar muito com a presença: "

print(f"{mensagem + lista_de_convidados[0]}")
print(f"{mensagem + lista_de_convidados[1]}")
print(f"{mensagem + lista_de_convidados[2]}")
print(f"{mensagem + lista_de_convidados[3]}")
print("Infelizmente o quarto convidado não poderá comparecer! ")
print(f"Felizmente temos outro convidado disponível")
del lista_de_convidados[3]
lista_de_convidados.append('eder')
print(lista_de_convidados)
print(f"{mensagem + lista_de_convidados[0]}")
print(f"{mensagem + lista_de_convidados[1]}")
print(f"{mensagem + lista_de_convidados[2]}")
print(f"{mensagem + lista_de_convidados[3]}")
lista_de_convidados.append("flavio")
lista_de_convidados.append("Paola")
lista_de_convidados.append("Lucas")
print(lista_de_convidados)
lista_de_convidados.insert(0, "Paulo")
lista_de_convidados.insert(3, "Ilana")
print(lista_de_convidados)
print("Comunico aos demais convidados que infelizmente"
      "não a mesa para todos, manteremos todos "
      "informados para um novo convite")
lista_de_convidados.pop(0)
lista_de_convidados.pop(4)
lista_de_convidados.pop(6)
lista_de_convidados.pop(3)
print(lista_de_convidados)
lista_de_convidados.pop(0)
print(lista_de_convidados)
lista_de_convidados.pop(0)
lista_de_convidados.pop(2)
print(lista_de_convidados)
print(f"gostaria de comunicar á: {lista_de_convidados[0]} e {lista_de_convidados[1]} que vocês continuam convidados"
      f"para o jantar,")
print("Atenciosamente seu anfitrião")
del lista_de_convidados[0]

print(lista_de_convidados)
del lista_de_convidados[0]
print(lista_de_convidados)

