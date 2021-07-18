def get_formatted_name(first_name, last_name, middle_name=""):
    """Devolve um nome completo formatado de forma elegante."""
    if middle_name:
        full_name = first_name + ' ' + middle_name + ' ' + last_name
    else:
        full_name = first_name + ' ' + last_name
        return full_name.title()


musician = get_formatted_name('john', 'hooker',)
jogador = get_formatted_name('eder', 'cantanhede', 'silva')
print(musician)
print(jogador)
