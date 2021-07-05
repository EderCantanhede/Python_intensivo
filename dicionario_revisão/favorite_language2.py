favorite_language = {
    'jen': ['python', 'ruby'],
    'sarah': ['C'],
    'edward': ['ruby', 'go'],
    'phil': ['python', 'haskel'],
}
# Esse primeiro laço armazena as chaves em "name = (keys)" e o valor em "languages = (values)"
for name, languages in favorite_language.items():
    print("\n" + name.title() + "'s favorite language are: ")
    for language in languages:  # Esse segundo laço armazena os valores de "languages = (values)" em "language"
        print("\t" + language.title())
