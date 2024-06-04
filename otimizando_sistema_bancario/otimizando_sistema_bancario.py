def deposito(saldo, extrato, valor, /):
    if valor > 0:
        saldo += valor
        extrato.append(f' Depósito:\t R$ {valor:.2f}')
        print(f'\n === Depósito de R$ {valor:.2f} realizado com sucesso! ===')
    else:
        print('Operação inválida! Tente novamente.')
    
    return saldo, extrato


def sacar(*, saldo, extrato, valor, LIMITE_SAQUES, limite_valor_saque, saques_efetuados):
    if valor > 0:
        if saldo >= valor and saques_efetuados < LIMITE_SAQUES and valor <= limite_valor_saque:
            saldo -= valor
            extrato.append(f' Saque:\t \t R$ {valor:.2f}')
            saques_efetuados += 1 
            print(f'\n === Saque de R$ {valor:.2f} realizado com sucesso! ===')
        elif saques_efetuados >= LIMITE_SAQUES:
            print('Limite de saques diário atingido!')
        elif valor > limite_valor_saque:
            print(f'Valor de saque excede o limite de R$ {limite_valor_saque:.2f} diários.')
        else:
            print('Saldo insuficiente!')
    else:
        print('Valor de saque inválido!')

    return saldo, extrato, saques_efetuados


def mostrar_extrato(saldo, /, *, extrato):
    print('\n =========== EXTRATO ===========\n')
    if extrato:
        for i in extrato:
            print(i)
    else:
        print('Não há movimentações.')
    print(f'\n Saldo atual:\t R$ {saldo:.2f}')
    print('\n ===============================\n')

def novo_usuario(usuarios):
    usuario = dict()
    
    cpf = int(input('Digite seu CPF (apenas números): '))
    if any(u['cpf'] == cpf for u in usuarios):
        print('Usuário existente.')
        return usuarios
    print(' === Usuário criado com sucesso! ===')
    
    nome = input('Digite o nome completo: ')
    data_nascimento = input('Digite a data de nascimento (dd-mm-aaaa): ')
    endereco = input('Digite o endereço (logradouro, nº - bairro, cidade/sigla estado): ')
        
    usuario['cpf'] = cpf
    usuario['nome'] = nome
    usuario['data de nascimento'] = data_nascimento
    usuario['endereco'] = endereco

    usuarios.append(usuario.copy())
    return usuarios

def criar_conta(usuarios, contas, agencia):
    cpf = int(input('Digite o CPF do usuário: '))
    usuario = next((u for u in usuarios if u['cpf'] == cpf), None)
    if usuario:
        numero_conta = len(contas) + 1  
        conta = {'agencia': agencia, 'numero_conta': numero_conta, 'usuario': usuario}
        contas.append(conta)
        print('\n === Conta criada com sucesso! ===')
        return contas
    else:
        print('Usuário não encontrado!')
        return contas

def listar_contas(contas):
    cpf = int(input('Digite o CPF do usuário: '))
    contas_usuario = [c for c in contas if c['usuario']['cpf'] == cpf]
    if contas_usuario:
        for conta in contas_usuario:
            print(f"Nome: {conta['usuario']['nome']}, Agência: {conta['agencia']}, Número da conta: {conta['numero_conta']}")
    else:
        print('Usuário não possui contas.')

def menu():
    print('''\n
 ============= MENU ============
              
  [1]\t Depósito  
  [2]\t Saque     
  [3]\t Extrato  
  [4]\t Novo Usuário
  [5]\t Nova Conta
  [6]\t Listar Contas
  [7]\t Sair      
              
 ============= ** ==============
Selecione uma opção:  ''') 
    return int(input().strip())

def main():
    AGENCIA = '0001'
    LIMITE_SAQUES = 3

    saldo = 0
    limite_valor_saque = 500
    extrato = []
    saques_efetuados = 0
    usuarios = []
    contas = []

    while True:
        opcao = menu()
        
        if opcao == 1:
            valor = float(input('Informe o valor do depósito: R$ '))
            saldo, extrato = deposito(saldo, extrato, valor)
        
        elif opcao == 2:
            valor = float(input('Informe o valor do saque: R$ '))
            saldo, extrato, saques_efetuados = sacar(
                saldo=saldo,
                extrato=extrato,
                valor=valor,
                LIMITE_SAQUES=LIMITE_SAQUES,
                limite_valor_saque=limite_valor_saque,
                saques_efetuados=saques_efetuados
            )

        elif opcao == 3:
            mostrar_extrato(saldo, extrato=extrato)
        
        elif opcao == 4:
            usuarios = novo_usuario(usuarios)

        elif opcao == 5:
            contas = criar_conta(usuarios, contas, AGENCIA)

        elif opcao == 6:
            listar_contas(contas)

        elif opcao == 7:
            print('\nObrigado por utilizar nossos serviços!')
            break

        else:
            print('Opção inválida! Tente novamente.')

main()