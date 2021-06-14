carros = ['subaru', 'toyota', 'monza', 'palio']
motos = ['kawasaki', 'ducati', 'suzuki', 'honda']
if carros == motos:
    print("True")
else:
    print("False")
    if carros and motos == str:
        print("Esses objetos são do type string!")
    else:
        print(f"Esses objetos são do tipo:{type(carros)}, {type(motos)}")
if carros or motos == type(list):
    print(f"Esses objetos são do tipo:{type(carros)}, {type(motos)}")
if carros or motos == list:
    for carro in carros:
        print(carro.title() + ",Esse código está ficando muito legal")
    for moto in motos:
        print(moto.title() + ", Estou começando a pegar pratica")
