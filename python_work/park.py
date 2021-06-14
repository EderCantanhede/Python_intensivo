idade = 12
if idade < 4:
    prece = 0
elif idade < 18:
    prece = 5
elif idade < 65:
    prece = 10
elif idade <= 65:
    prece = 5
print("O custo da sua entrada é $" + str(prece) + ".")
