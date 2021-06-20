linguagens_favorita = {
    'jen': 'python', 'bia': 'java', 'sarah': 'java.js',
    'phil': 'C++', 'edward': 'C#', 'carlos': 'ruby'
}
amigos = ['phil', 'sarah']
for name in sorted(linguagens_favorita.keys()):
    print(name.title())
    if name in amigos:
        print("Hi " + name.title() + ", I see your favorite language is "
              + linguagens_favorita[name].title() + " !")
if 'erin' not in linguagens_favorita.keys():
    print("Erin, please take our poll! ")
print(name.title() + ", thank you for talking the poll.")
for linguagens in linguagens_favorita.values():
    print(linguagens.title())
for linguagens in set(linguagens_favorita.values()):
    print(linguagens.title())


