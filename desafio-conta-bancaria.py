# sistema bancário com as operações: sacar, depositar e visualizar extrato
# Deve ser possível depositar valores positivos (proibe negativos)
# Todos os depósitos devem ser armazenados em uma variável e exibidos na operação de extrato
# Caso o usuário não tenha saldo em conta, o sistema deve exibir uma mensagem
# informando que não será possível sacar o dinheiro por falta de saldo.
# Todos os saldos devem ser armazenados em uma variável e exibidos na operação extrato.
# Extrato: essa operação deve listar todos os depósitos e saques realizados na conta.
# No fim da listagem deve ser exibido o saldo atual da conta.
# Os valores devem ser exibidos utilizando o formato R$ XXX.XXX, exemplo: 1500.45 = R$ 1500.45

menu = """

[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

=> """

<<<<<<< HEAD
valor = 0
=======
>>>>>>> af10b3b7b96e3879de02154348f05b46e64f32b4
saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3
<<<<<<< HEAD
=======
valor = 0
>>>>>>> af10b3b7b96e3879de02154348f05b46e64f32b4

while True:
    
    opcao = input(menu)

    if opcao == "d":
        print("Depósito")
        valor = float(input("Valor para depósito: "))
        if valor > 0:
            saldo = saldo + valor
            print(f"Depósito de R${valor:.2f} feito com sucesso.")
            extrato = extrato + f"Depósito: R${valor:.2f}\n"
        else:
            print("Operação inválida. O valor informado é inválido.")


    elif opcao == "s":
        print("Saque")
        valor = float(input("Valor para sacar: "))
        
        excedeu_saldo = valor > saldo
        excedeu_limite = valor > limite
        excedeu_saques = numero_saques >= LIMITE_SAQUES
        
        if excedeu_saldo:
            print("Operação falhou! Você não tem saldo suficiente.")

        elif excedeu_limite:
            print("Operação falhou! O valor do saque excedeu o limite.")

        elif excedeu_saques:
            print("Operação falhou! Você excedeu o limite de saques.")
        
        elif valor > 0:
            saldo = saldo - valor
            print(f"Saque de R${valor:.2f} feito com sucesso.")
            extrato = extrato + f"Saque: R${valor:.2f}\n"
            numero_saques += 1
            print(f"Você fez {numero_saques} saques.")

        else:
            print("Operação inválida. O valor informado é inválido.")
            
    elif opcao == "e":
        print("\n================== EXTRATO ==================")
        print("Não foram realizadas movimentações." if not extrato else extrato) #se o extrato não está vazio ele mostra extrato
        print(f"Saldo: R${saldo:.2f}")
        print("=============================================")

    elif opcao == "q":
        break

    else:
        print("Operação inválida, por favor selecione novamente a operação desejada.")