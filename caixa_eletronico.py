def separator():
    print("*" * 80)


def separator_saldo():
    print("=" * 80)


saldo = float(10)
saldo_real = round(saldo, 2)

extrato = []


def mostrarSaldo():
    print(f"O saldo atual da conta é de: R$ {saldo_real} ".replace(".", ","))


option = 0
while option != 5:
    separator()
    print("Bem vindo ao Banco Bruno")
    print("Escolha qual operação deseja realizar")
    print("[1] Consultar saldo")
    print("[2] Deposito")
    print("[3] Saque")
    print("[4] Extrato ")
    print("[5] Sair")

    separator()

    option = int(input("Digite a opção que deseja realizar: "))

    if option == 1:
        sub_option = 0

        while sub_option != "":
            separator_saldo()
            print("")
            print("")
            mostrarSaldo()
            print("")
            print("")
            separator_saldo()
            sub_option = str(
                input("Aperte ENTER para voltar ao menu principal"))
            if sub_option != "":
                print("Opção inválida, Aperte ENTER para voltar ao menu principal")
            else:
                print("Voltando ao menu principal...")
    elif option == 2:
        sub_option = 0
        while sub_option != "":
            print("")
            print("")
            print("Digite o valor que deseja depositar: ")
            deposito = float(input("-").replace(",", "."))
            if deposito > 0:
                saldo_real += deposito
                print(
                    f"Valor de {str(deposito).replace(".", ",")} depositado com sucesso.")
                sub_option = str(
                    input("Aperte ENTER para voltar ao menu principal"))
                extrato.append(
                    f"Depósito: +{str(deposito).replace('.', ',')} R$")

            else:
                print("Deposito inválido, digite um valor válido.")
                sub_option = str(
                    input("Aperte ENTER para voltar ao menu principal"))
    elif option == 3:
        sub_option = 0
        while sub_option != "":
            print(f"Saldo atual de: {saldo_real}")
            print("-")
            print("-")
            print("-")
            print("-")
            saque = float(
                input("Digite o valor que deseja sacar: ").replace(",", "."))
            saque = round(saque, 2)

            if saque <= 0 or saldo_real <= 0:
                print(f"Valor inválido")

                sub_option = str(input("Aperte ENTER para voltar ao menu"))
            elif saque > saldo_real:
                input(
                    "Transação indisponivel! Você não pode sacar um valor maior do que tem disponivel.")
            elif saque > 0 and saldo_real > 0:
                print(f"É possivel realizar o saque")
                saldo_real -= saque
                print(
                    f"Foi sacado o valor de {str(saque).replace(".", ",")} R$ e restou na conta {str(saldo_real).
                                                                                                 replace(".", ",")} R$")

                extrato.append(f"Saque: -{str(saque).replace('.', ',')} R$")

                sub_option = str(input("Aperte ENTER para voltar ao menu"))
    elif option == 4:
        separator()
        print("Extrato da conta:")
        for transacao in extrato:
            print(transacao)
        separator()
        input("Aperte ENTER para voltar ao menu principal")

    elif option == 5:
        print(f"Aplicação encerrada...")

    else:
        print("Digite uma opção válida.")
