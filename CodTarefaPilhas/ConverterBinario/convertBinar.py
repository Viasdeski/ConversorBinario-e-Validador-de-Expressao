import os

from classes import Binario

converter = True

while converter:

    os.system('clear') # Será criado uma funcao para selecionar o OS e assim atribuir corretamente o comando.

    bin = Binario()
    binario = []

    try:
        numero = input("Qual número deseja converter para binário: ")
        numero = int(numero)
    except ValueError:
        print('Valor inválido. Lmebre-se de digitar um número inteiro')

    bin.dec2bin(numero)

    while len(bin) > 0:
        binario.append(bin.pop())

    binario = ''.join(map(str, binario))

    print(f'O número {numero} em binário equivale a: {binario}')

    os.system('clear')

    menu = {
        'Menu': {
            'pergunta': 'Deseja converter outro número?',
            'opcoes': {
                '(1)': 'SIM',
                '(2)': 'NÃO'
            }
        }
    }

    for chavePerg, chaveResp in menu.items():
        print(chaveResp['pergunta'])

        for respChave, respValor in chaveResp['opcoes'].items():
            print(f'{respChave}:{respValor}')

        respUsuario = input('Sua escolha: ')

        os.system('clear')

        if respUsuario.isnumeric():
            if respUsuario == '1':
                break
            elif respUsuario == '2':
                converter = False
                print('Encerrando conversor...')
        else:
            print('O valor deve ser um número inteiro')
