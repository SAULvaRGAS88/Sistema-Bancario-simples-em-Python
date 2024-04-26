from datetime import datetime

saldo = 0
limite = 500
extrato = []
numero_saques = 0
LIMITE_SAQUES = 3

def depositar(valor):
    global saldo, extrato
    saldo += valor
    data_hora_atual = datetime.now()
    extrato.append((data_hora_atual, f"Depósito: R$ {valor:.2f}"))

def sacar(valor):
    global saldo, extrato, numero_saques
    if valor > saldo:
        print("Operação falhou! Você não tem saldo suficiente.")
        return False
    elif valor > limite:
        print("Operação falhou! O valor do saque excede o limite.")
        return False
    elif numero_saques >= LIMITE_SAQUES:
        print("Operação falhou! Número máximo de saques excedido.")
        return False
    elif valor <= 0:
        print("Operação falhou! O valor informado é inválido.")
        return False
    else:
        saldo -= valor
        numero_saques += 1
        data_hora_atual = datetime.now()
        extrato.append((data_hora_atual, f"Saque: R$ {valor:.2f}"))
        return True

def exibir_extrato():
    global extrato, saldo
    print("\n================ EXTRATO ================")
    if not extrato:
        print("Não foram realizadas movimentações.")
    else:
        for data_hora, transacao in extrato:
            print(f"{data_hora.strftime('%H:%M:%S %d/%m/%Y')} - {transacao}")
    print(f"\n>>> Saldo: R$ {saldo:.2f} <<<")
    print("==========================================")


menu = """
[D] Depositar
[S] Sacar
[E] Extrato
[Q] Sair

=> """

while True:
    opcao = input(menu).lower()

    if opcao == "d":
        valor = float(input("Informe o valor do depósito: "))
        depositar(valor)
        print(f'Depósito realizado com sucesso!\n---> Depósito: R$ {valor:.2f}')

    elif opcao == "s":
        valor = float(input("Informe o valor do saque: "))
        if sacar(valor):
            print(f'Saque realizado com sucesso!\n---> Saque: R$ {valor:.2f}')
        else:
            print("Operação de saque falhou!")

    elif opcao == "e":
        exibir_extrato()

    elif opcao == "q":
        break

    else:
        print("Operação inválida, por favor selecione novamente a operação desejada.")
