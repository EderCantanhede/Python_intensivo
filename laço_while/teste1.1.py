controle = ""
while controle != 's':
    print("a.pagar: ")
    print("b.receber: ")
    print("c.consultar: ")
    print("\n")
    if controle == 'a':
        print("Oque você gostaria de pagar?")
    elif controle == 'b':
        print("Quanto você deseja sacar? ")
    elif controle == 'c':
        print("O que você gostaria de consultar? ")
    print("s.sair: ")
    controle = input("digite a opção desejada: ")
print("loop encerrado.")
