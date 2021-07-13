respostas = {}
polling_active = True
while polling_active:
    name = input("\nWhat is your name? ")
    resposta = input("Which mountain wold you like to climb someday? ")
    respostas[name] = resposta
    repeat = input("Would you like to let another person respond? (yes/ no)")
    if repeat == 'no':
        polling_active = False
        print("\n---Poll Results---")
        for name, resposta in respostas.items():
            print(name + " would like te climb " + str(resposta) + ".")
