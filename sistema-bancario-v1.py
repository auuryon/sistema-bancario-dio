def menu():
  menu = f'''
{' MENU '.center(40, '-')}

[d]\tDepositar
[s]\tSacar
[e]\tExtrato
[nc]\tNova conta
[lc]\tLista contas
[nu]\tNovo usuário
[q]\tSair

{''.center(40, '-')}
=> '''
  return input(menu)


def depositar(saldo, valor, extrato, /):
  if valor >= 1:
    saldo += valor
    extrato += f'Depósito:\tR$ {valor:.2f}\n'

  else:
    print('\nOperação falhou! Valores para depósito inválidos.')

  return saldo, extrato


def sacar(* , saldo, valor, extrato, numero_saques, limite, limite_saques):
  if numero_saques >= limite_saques:
    print('\nO limite de saques diários foi atingido. Aguarde até o próximo dia.')

  elif valor > limite:
    print('\nOperação inválida! O limite máximo de saque é R$ 500.00')

  elif valor > saldo:
    print('\nNão será possível sacar o dinheiro por falta de saldo.')

  elif valor > 0:
    numero_saques += 1
    saldo -= valor
    extrato += f'Saque:\t\tR$ {valor:.2f}\n'

  else:
    print('\nOperação falhou! o valor informado é inválido.')

  return saldo, extrato, numero_saques


def exibir_extrato(saldo, /, *,extrato):
  print(f'''
{' EXTRATO '.center(40, '-')}
{extrato}

Saldo:\t\tR$ {saldo:.2f}
{''.center(40, '-')}
''')


def criar_usuario(usuarios):
  cpf = input('Informe o CPF (somente número): ')
  usuario = filtrar_usuario(cpf, usuarios)

  if usuario:
    print('\nJá existe usuário com esse CPF!')
    return
  
  nome = input('Informe o nome completo: ')
  data_nascimento = input('Informe a data de nascimento (dd-mm-aaaa): ')
  endereco = input('Informe o endereço (logradouro, nro - bairro - cidade/sigla estado): ')

  usuarios.append({'nome': nome, 'data_nascimento': data_nascimento, 'cpf': cpf, 'endereco': endereco})

  print('\nUsuário criado com sucesso!')


def filtrar_usuario(cpf, usuarios):
  usuarios_filtrados = [usuario for usuario in usuarios if usuario["cpf"] == cpf]
  return usuarios_filtrados[0] if usuarios_filtrados else None


def criar_conta(agencia, contas, usuarios):
  cpf = input('Informe o CPF do usuário: ')
  usuario = filtrar_usuario(cpf, usuarios)

  if not usuario:
    print('\nNão existe usuário com esse CPF!')
    return
  
  numero_conta = len(contas) + 1

  contas.append({'agencia': agencia, 'numero_conta': numero_conta,'usuario': usuario})

  print('\nConta criada com sucesso!')


def listar_contas(contas):
  for conta in contas:
    linha = f'''
Agência:\t{conta['agencia']}
C/C:\t\t{conta['numero_conta']}
Titular:\t{conta['usuario']['nome']}
    '''
    print(''.center(40, '='))
    print(linha)


def main():
  LIMITE = 500
  LIMITE_SAQUES = 3
  AGENCIA = '0001'

  saldo = 0
  extrato = ''
  numero_saques = 0
  usuarios = []
  contas = []

  while True:
    opcao = menu()

    if opcao == 'd':
      valor = float(input('\nQual o valor do depósito? R$ '))
      saldo, extrato = depositar(saldo, valor, extrato)

    elif opcao == 's':
      valor = float(input('\nQual o valor de saque? R$ '))
      saldo, extrato, numero_saques = sacar(
        saldo=saldo,
        valor=valor,
        extrato=extrato,
        numero_saques=numero_saques,
        limite=LIMITE,
        limite_saques=LIMITE_SAQUES,
        )

    elif opcao == 'e':
      exibir_extrato(saldo, extrato=extrato)

    elif opcao == 'nc':
      criar_conta(AGENCIA, contas, usuarios)

    elif opcao == 'lc':
      listar_contas(contas)

    elif opcao == 'nu':
      criar_usuario(usuarios)
    
    elif opcao == 'q':
      break

    else:
      print('\nOperação inválida! Por favor selecione novamente a operação desejada.')


main()