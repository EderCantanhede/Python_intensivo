# O objetivo desse exercício era eliminar possíveis espaços entre as aspas
# usando os métodos " rstrip, lstrip, strip, e uma tabulação usando '\t'
# Só faltou '\n' que significa quebra de linha

var = str(" Estudar python é muito legal ")
print(var)
print(var.rstrip())
print(var.lstrip())
print(var.strip())
print(f"\t{var}")
