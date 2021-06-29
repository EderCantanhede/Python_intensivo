pessoas = {
    'illana': {'musica favorita': 'pop, ', 'robbie': 'estudar programação', 'comida favorita': 'lasanha'},
    'helena': {'musica favorita': 'sertanejo, ', 'robbie': 'colecionar antiguidades', 'comida favorita': 'churrasco'},
    'beto': {'musica favorita': 'pop rock, ', 'robbie': 'patinar', 'comida favorita': 'japonesa'},
    'carlos': {'musica favorita': 'hip hop, ', 'robbie': 'andar de bike', 'comida favorita': 'hamburger'},
}
for people, lista in pessoas.items():
    print("\nEsses jovens são:" + people)
    robbies = lista['musica favorita'] + " " + lista['robbie']
    do_que_gostam = lista['comida favorita']
    print("\tCaracterísticas dos jovens: " + robbies.title())
    print("\tE do que eles gostam: " + do_que_gostam.title())
