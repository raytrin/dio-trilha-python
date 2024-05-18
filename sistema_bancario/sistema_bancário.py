menu = '''

 ==== MENU ====
              
  [1] Depósito  
  [2] Saque     
  [3] Extrato   
  [4] Sair      
              
 ===== ** =====

'''
saldo = 0
limite = 500
LIMITE_SAQUES = 3
extrato = ''




while True:
    print(menu)
    opcao = int(input('Selecione uma opção: '))

    if opcao == 1:
        deposito = float(input('Digite o valor do depósito: R$ '))
        if deposito > 0:
            saldo += deposito
            extrato += f'Depósito {deposito:.2f}\n'
            print(f'Depósito de R${deposito:.2f} realizado com sucesso!')
        elif deposito < 0:
            print('Operação inválida! Tente novamente.')
        else:
            print('Operação não realizada! Por favor, informe um valor válido.')

    elif opcao == 2:
        saque = float(input('Digite o valor do saque: R$'))

        if (LIMITE_SAQUES > 0) and (saque < saldo) and (saque <= limite) and (saque > 0):
            saldo -= saque
            extrato += f'Saque: R${saque:.2f}\n'
            LIMITE_SAQUES -= 1
            print(f'Saque de R${saque:.2f} realizado com sucesso!\n')
        
        elif LIMITE_SAQUES == 0:
            print(f'Você atingiu o número máximo de 3 saques diários.')

        elif saque > limite:
            print(f'O valor máximo permitido para saque é de R${limite:.2f}. Por favor, tente novamente.')

        elif saque > saldo:
            print('Você não tem saldo suficiente para realizar essa operação. Tente novamente.')

        elif saque < 0:
            print('Operação inválida! Tente novamente.')    


    elif opcao == 3:
        print('=============      EXTRATO       =============\n')

        print(extrato)

        print(f'Saldo atual: R${saldo:.2f}\n')
        print('====================  **  ====================')   

    elif opcao == 4:
        print('Obrigado(a) por utilizar nossos serviços. Volte sempre!')
        break
    else:
        print('Operação inválida. Tente novamente!')
        