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

print(50 * '-')
print('Bem vindo a locadora BR')
print(50 * '-')

def mostrar_lista_de_veiculos(lista_de_veiculos):
    lista_de_veiculos_ordenada = sorted(lista_de_veiculos)
    for contador, veiculos in enumerate(lista_de_veiculos_ordenada):
        print(f'[{contador}] {veiculos[0]} - R$ {veiculos[1]} por dia.')

mostrar_lista_de_veiculos(veiculos_disponiveis)

