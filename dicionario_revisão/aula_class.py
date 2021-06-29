# Uma classe é uma abstração de alguma "coisa", que possui um estado
# e comportamento. Um estado é definido por um conjunto de variáveis
# chamadas de atributos. Esses estados podem ser alterados por meio de "ações"
# sobre o objeto, que definem seu comportamento. Essas ações são funções chamada de "métodos"

class Carro:
    def __init__(self):
        self.ano = None

    pass


fusca = Carro()
brasilia = Carro()

fusca.ano = 1986
fusca.modelo = 'fusca'
fusca.cor = 'preto'

brasilia.ano = 1981
brasilia.modelo = 'Brasilia'
brasilia.cor = 'amarela'

novo_fusca = fusca
print("Fusca igual a brasilia ? > ", fusca == brasilia)
print("Fusca igual a novo_fusca ? > ", fusca == novo_fusca)
fusca.ano += 10
print("fusca.ano = ", fusca.ano)
print("novo_fusca.ano = ", novo_fusca.ano)
