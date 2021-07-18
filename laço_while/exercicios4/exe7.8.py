"""
7.8 – Lanchonete: Crie uma lista chamada sandwich_orders e a preencha com
os nomes de vários sanduíches. Em seguida, crie uma lista vazia chamada
finished_sandwiches. Percorra a lista de pedidos de sanduíches com um laço e
mostre uma mensagem para cada pedido, por exemplo, Preparei seu
sanduíche de atum. À medida que cada sanduíche for preparado, transfira-o
para a lista de sanduíches prontos. Depois que todos os sanduíches estiverem
prontos, mostre uma mensagem que liste cada sanduíche preparado.
"""
sandwich_orders = ['presunto', 'pastrami', 'atum', 'pastrami', 'mortadela', 'carne ceca', 'bife', 'pastrami']
finished_sandwiches = []
print("\nNão temos mais pastrami!")
while sandwich_orders:
    while 'pastrami' in sandwich_orders:
        sandwich_orders.remove('pastrami')
    pedidos_cliente = sandwich_orders.pop()
    print("pedido confirmado " + pedidos_cliente.title())
    finished_sandwiches.append(pedidos_cliente)
    print("\nOs seguintes pedidos estão confirmados: ")
    for finished_sandwiche in finished_sandwiches:
        print(finished_sandwiche.title())

