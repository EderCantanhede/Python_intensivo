"""
8.6 – Nomes de cidade: Escreva uma função chamada city_country() que
aceite o nome de uma cidade e seu país. A função deve devolver uma string
formatada assim: "Santiago, Chile"
Chame sua função com pelo menos três pares cidade-país e apresente o valor
devolvido.
"""


def city_country(x, y):
    """Devolve o nome de cidades"""
    city = x, y
    return city


city1 = str(city_country('santiago', 'chile'))
print(city1.title())



