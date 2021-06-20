Glossario = {
    'hello': 'olá', 'the': 'O,os,a,as', 'to': 'para', 'of': 'de', 'and': 'e',
    'A': 'um,uma', 'in': 'em,dentro', 'is': 'é', 'it': 'este', 'you': 'você',
    'that': 'que,aquele', 'he': 'ele', 'was': 'era,estava', 'for': 'por,para',
}
print("hello: " + Glossario['hello'] + "\n")
print("the: " + Glossario['the'] + "\n")
print("to: " + Glossario['to'])
for word in Glossario.keys():
    print(word.title())
