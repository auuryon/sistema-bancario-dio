""" OPERAÇÃO DE DEPÓSITO
Deve ser possível depositar valores positivos para a minha conta bancária. A v1 do projeto trabalha apenas com 1 usuário,
dessa forma não precisamos nos preocupar em identificar qual é o número da agência e conta bancária. Todos os depósitos
devem ser armazenados em uma variável e exibidos na operação de extrato.
"""

""" OPERAÇÃO DE SAQUE
O sistema deve permitir realizar 3 saques diários com limite máximo de R$ 500,00 por saque. Caso o usuário não tenha
saldo em conta, o sistema deve exibir uma mensagem informando que não será possível sacar o dinheiro por falta de
saldo. Todos os saques devem ser armazenados em uma variável e exibidos na operação de extrato.
"""

""" OPERAÇÃO DE EXTRATO
Essa operação deve listar todos os depósitos e saques realizados na conta. No fim da listagem deve ser exibido o saldo atual da conta.
Os valores devem ser exibidos utilizando o formato R$ xxx.xx, exemplo: 1500.45 = R$ 1500.45
"""

menu = f'''
{' MENU '.center(40, '-')}

[d] - Depositar
[s] - Sacar
[e] - Extrato
[q] - Sair

{''.center(40, '-')}
'''

saldo = 10
limite = 500
extrato = ''
numero_saques = 0
LIMITE_SAQUES = 3

while True:

  opcao = input(menu)

  if opcao == 'd':
    valor = float(input('\nQual o valor do depósito? R$ '))

    if valor >= 1:
      saldo += valor
      extrato += f'Depósito: R$ {valor:.2f}\n'

    else:
      print('\nOperação falhou! Valores para depósito inválidos.')

  elif opcao == 's':
    valor = float(input('\nQual o valor de saque? R$ '))

    if numero_saques >= LIMITE_SAQUES:
      print('\nO limite de saques diários foi atingido. Aguarde até o próximo dia.')

    elif valor > limite:
      print('\nOperação inválida! O limite máximo de saque é R$ 500.00')

    elif valor > saldo:
      print('\nNão será possível sacar o dinheiro por falta de saldo.')

    elif valor > 0:
      numero_saques += 1
      saldo -= valor
      extrato += f'Saque: R$ {valor:.2f}\n'

    else:
      print('\nOperação falhou! o valor informado é inválido.')

  elif opcao == 'e':
    print(f'''
{' EXTRATO '.center(40, '-')}

Saldo: R$ {saldo:.2f}

{extrato}

{''.center(40, '-')}
''')

  elif opcao == 'q':
    break

  else:
    print('\nOperação inválida! Por favor selecione novamente a operação desejada.')