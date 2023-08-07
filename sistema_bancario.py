import os
from time import sleep

menu = f"""
Escolha a operação desejada:
[1] Depósito
[2] Saque
[3] Extrato
[0] Sair
"""

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

print(""" 
    =-=-=-=-=-=-=-=-=-=-=-=-=-=-=
            Banco Digital        
    =-=-=-=-=-=-=-=-=-=-=-=-=-=-=""")

while True:
    print(f"\nSaldo: R${saldo}")
    while True:
        op_str = input(menu)
        if op_str.isdigit():
            op = int(op_str)
            if op in [1, 2, 3, 4, 0]:
                break
        print("Opção inválida! Por favor, tente novamente!")

    if op == 0:
        break

    elif op == 1:
        valor_deposito = int(input("Informe o valor do depósito: R$"))
        while valor_deposito <= 0:
            valor_deposito = int(input("Valor inválido. Informe o valor do depósito: R$"))
            
        saldo += valor_deposito
        extrato += f"Depósito    R${valor_deposito}\n"
        print("Depósito realizado com sucesso!")
        sleep(1)
        os.system('cls' if os.name == 'nt' else 'clear')

    elif op == 2:
        valor = int(input("Informe o valor do saque: R$"))

        excedeu_limite = numero_saques == LIMITE_SAQUES

        excedeu_saque = valor > 500
        
        saldo_insuficiente = valor > saldo

        if excedeu_saque:
            print("Ocorreu um erro! Limite de saque excedido.")
            sleep(1)
            os.system('cls' if os.name == 'nt' else 'clear')

        elif excedeu_limite:
            print("Ocorreu um erro! Limite diario de saque excedido.")
            sleep(1)
            os.system('cls' if os.name == 'nt' else 'clear')

        elif saldo_insuficiente:
            print("Ocorreu um erro! Não há saldo suficiente.")
            sleep(1)
            os.system('cls' if os.name == 'nt' else 'clear')

        elif valor > 0:
            saldo -= valor
            extrato += f"Saque       R${valor}\n"
            numero_saques += 1
            print("Saque realizado com sucesso!")
            sleep(1)
            os.system('cls' if os.name == 'nt' else 'clear')
        
        else:
            print("Ocorreu um erro! Valor informado é inválido.")
            sleep(1)
            os.system('cls' if os.name == 'nt' else 'clear')

    elif op == 3:
        print(" EXTRATO ".center(35, "="))
        print("Não foram realizadas movimentações!" if not extrato else extrato)
        print(f"______________________\nSaldo:      R${saldo}\n")
        print("".center(35, "="))
        input("Pressione <enter> para continuar")
        sleep(1)
        os.system('cls' if os.name == 'nt' else 'clear')


