menu_geral = '''
    ========SISTEMA BANCÁRIO========
        [1] Depositar
        [2] Sacar
        [3] Extrato
        [4] Saldo
        [0] Fechar
    ================================
'''
menu_extrato = '''
    ========EXTRATO=========
'''
menu_depósito = '''
    ========DEPÓSITO========
'''
menu_saque = '''
    ========SAQUE===========
'''

opcao = None
saldo = 0
valor_deposito = 0
valor_saque = 0
extrato = f'Aqui está o seu extrato: \n'
LIMTE_SAQUE = 3
saques_diarios = 0

while opcao != 0:
    print(menu_geral)
    opcao = int(input('Selecione a opção desejada: '))

    if opcao == 1:
        print(menu_depósito)
        valor_deposito = float(input('Digite o  valor de Depósito: '))
        saldo = saldo + valor_deposito
        extrato = extrato + f'Depósito: R$ {valor_deposito:.2f}\n'
        print('Seu depósito foi realizado com sucesso!\n')

    elif opcao == 2 :
        if (saques_diarios != LIMTE_SAQUE) and (valor_deposito > valor_saque):
            print(menu_saque)
            valor_saque = float(input('Digite o  valor de Saque: '))
            saldo = saldo - valor_saque
            saques_diarios = saques_diarios + 1
            extrato = extrato + f'Saque: R$ {valor_saque:.2f}\n'
            print('Seu saque foi realizado com sucesso!\n')

        else: 
            print('Você já sacou três(3) vezes, e não pode mais retirar dinheiro. Seus saques serão restaurados às 0h de amanhã;')

    elif opcao == 3:
        print(menu_extrato)
        print(extrato + f'Seu saldo é de R$ {saldo:.2f}')

    elif opcao == 4:
        print(f'Seu saldo é de {saldo:.2f}')

    elif opcao == 5:
        print('Obrigado por usar esse sistema bancário. Até mais!')
        break
    
    else:
        print('Essa opção não é válida! Selecione uma opção correta!')