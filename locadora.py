veiculos_disponiveis = [
    ('Ford Mustang', 220),
    ('Chevrolet Camaro', 250),
    ('Toyota Corolla', 180),
    ('Honda Civic', 175),
    ('Hyundai HB20S', 80),
    ('Volkswagen Golf', 100),
    ('Fiat Mobi', 75),
    ('Chevrolet Onix', 96),
    ('Audi A4', 160),
    ('Honda PCX(moto)',45)
    ]
veiculos_alugados =[]

def mostrar_lista_de_veiculos(lista_de_veiculos):
    lista_de_veiculos_ordenada = sorted(lista_de_veiculos)
    for contador, veiculos in enumerate(lista_de_veiculos_ordenada):
        print(f'[{contador}] {veiculos[0]} - R$ {veiculos[1]} por dia.')

print(68 * '-')
print('Bem vindo a locadora BR'.center(68))
print(68 * '-')

while True:

    print('O que deseja fazer?'.center(68).upper())
    print('0 - Mostrar portfolio | 1 - Alugar um veículo | 2 - Devolver um veículo')
    try:
        operacao = int(input())
    except:
        print('ERRO, você digitou algum valor invalido!'.center(68))



