import time

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
veiculos_disponiveis.sort()
veiculos_alugados =[]
def mostrar_portfolio():
    print(68 * '-')
    mostrar_lista_de_veiculos(veiculos_disponiveis)
    print(68 * '-')
def alugar_um_veiculo():
    print(68 * '-')
    mostrar_lista_de_veiculos(veiculos_disponiveis)
    print(68 * '-')
    print('Escolha o código do veículo que deseja alugar.')
    codigo_veiculo = int(input())
    print('Por quantos dias você deseja alugar este veiculo?')
    dias = int(input())

    print(f'Você escolher {veiculos_disponiveis[codigo_veiculo][0]} por {dias} dias.')
    print(f'O aluguel totalizaria R$ {dias * veiculos_disponiveis[codigo_veiculo][1]}. Deseja alugar?')
    print('0 - SIM | 1 - NÃO')
    confirmacao = int(input())

    if confirmacao == 0:
        print(f'Parabéns, você alugou o {veiculos_disponiveis[codigo_veiculo][0]} por {dias} dias')
        veiculos_alugados.append(veiculos_disponiveis.pop(codigo_veiculo))


def devolver_um_veiculo():
    if len(veiculos_alugados) == 0:
        print('Não há carros para devolver')
    else:
        print('Segue a lista de carros alugados. Qual você deseja devolver?')
        mostrar_lista_de_veiculos(veiculos_alugados)
        print('Escolha o código do carro que deseja devolver:')
        codigo_veiculo_devolucao = int(input())
        if codigo_veiculo_devolucao == 0:
            print(f'Obrigado por devolver o veículo {veiculos_alugados[codigo_veiculo_devolucao][0]}')
            veiculos_disponiveis.append(veiculos_alugados.pop(codigo_veiculo_devolucao))


def mostrar_lista_de_veiculos(lista_de_veiculos):

    for contador, veiculos in enumerate(lista_de_veiculos):
        print(f'[{contador}] {veiculos[0]} - R$ {veiculos[1]} por dia.')


# Inicio do programa
print(68 * '-')
print('Bem vindo a locadora BR'.center(68))
print(68 * '-')

while True:

    print('O que deseja fazer?'.center(68).upper())
    print('0 - Mostrar portfolio | 1 - Alugar um veículo | 2 - Devolver um veículo')
    try:
        operacao = int(input())
        if operacao == 0:
            mostrar_portfolio()
        elif operacao == 1:
            alugar_um_veiculo()
        elif operacao == 2:
            devolver_um_veiculo()

    except:
        print('ERRO, você digitou algum valor invalido, tente novamente!'.center(68))
        print('Reiniciando...')
        time.sleep(1)