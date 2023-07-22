# Mensagem de boas-vindas
print("Olá Usuário, Seja Bem Vindo!")
print('\n')

# Menu de operações
menu_operacao = '''
O que você deseja realizar:

[1] - Depósito
[2] - Saque
[3] - Extrato
[4] - Sair
'''

# Variáveis de controle
saldo = 0
limite = 500
extrato = []  # Lista para armazenar o extrato das operações
numero_saques = 0
LIMITE_SAQUE = 3

# Loop principal
while True:
    # Exibir o menu de operações e obter a opção escolhida pelo usuário
    opcao = input(menu_operacao)

    # Opção: Depósito
    if opcao == '1':
        try:
            valor = float(input("Informe o valor do depósito: "))
            if valor > 0:
                saldo += valor
                extrato.append(f'Depósito R$ {valor:.2f}')
            else:
                print('O valor informado é inválido')
        except ValueError:
            print('Insira um valor numérico válido.')

    # Opção: Saque
    elif opcao == '2':
      try:
          valor = float(input("Informe o valor do saque: "))
          if valor <= 0:
              print('O valor informado é inválido.')
          elif valor > saldo:
              print('Saldo insuficiente. Verifique seu saldo antes de fazer o saque.')
          elif valor > limite:
              print('O valor do saque excedeu o limite diário.')
          elif numero_saques >= LIMITE_SAQUE:
              print('Número máximo de saques diários atingido.')
          else:
              saldo -= valor
              extrato.append(f'Saque R$ {valor:.2f}')
              numero_saques += 1
              print(f'Saque de R$ {valor:.2f} realizado com sucesso.')
      except ValueError:
          print('Insira um valor numérico válido.')


    # Opção: Extrato
    elif opcao == '3':
        print('========= Extrato ==========')
        if extrato:
            for movimentacao in extrato:
                print(movimentacao)
        else:
            print('Não foram realizadas movimentações.')
        print(f'\nSaldo: R$ {saldo:.2f}')
        print('============================')

    # Opção: Sair
    elif opcao == '4':
        print('Aguarde!....')
        print('Você está saindo do ambiente.')
        break

    # Opção inválida
    else:
        print('Operação inválida, por favor selecione a operação desejada')