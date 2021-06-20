linguagens_favoritas = {'jen': 'python', 'sarah': 'C', 'edward': 'ruby', 'eder': 'java.js',
                        'phil': 'python', 'allan': 'C#'
                        }
print("sarah's linguagem favorita é " +
      linguagens_favoritas['sarah'].title() + ".")
for name, linguages in linguagens_favoritas.items():
    print(name.title() + " linguagens favorita é " + linguages.title() + ".")

