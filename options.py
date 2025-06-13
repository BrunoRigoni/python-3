option = 0  # A OPÇÃO É IGUAL A ZERO
number = [1, 2, 3, 4, 5, 6, 7, 8, 9,]


def err():
    print("Erro! Digite uma opção válida.")

# ENQUANTO A OPÇÃO NÃO FOR IGUALA  3, SEGUE A APLICAÇÃO


while option != 4:
    print("======= MENU PRINCIPAL =======")
    print("[1] - Adicionar novo número")
    print("[2] - Mostrar números")
    print("[3] - Números pares ou impares")
    print("[4] - Sair")
    print("==============================")
    option = int(input("Escolha uma opção: "))

    if option == 1:
        sub_option = 0
        while sub_option != 2:
            print("[1] Adicionar novo número a lista ")
            print("[2] sair ")
            sub_option = int(input("Digite a opção que deseja realizar: "))
            if sub_option == 1:
                add_number = int(
                    input("Digite o número que deseja adicionar: "))
                number.append(add_number)
            elif sub_option == 2:
                print("Voltando ao menú principal...")
            else:
                err()
    elif option == 2:
        sub_option = 0
        while sub_option != 2:
            print("[1] Ver itens ")
            print("[2] Sair ")
            sub_option = int(input("Digite a opção que deseja realizar: "))
            if sub_option == 1:
                for list_numbers in number:
                    print(list_numbers)
            elif sub_option == 2:
                print("Saindo da aplicação...")
            else:
                err()

        print(f"Aqui estão os números que foram adicionados a lista: {number}")
    elif option == 3:
        sub_option = 0
        while sub_option != 3:
            print("[1] - Ver números pares")
            print("[2] - Ver números impares")
            print("[3] - Sair")
            sub_option = int(input("Digite a opção que deseja realizar: "))

            if sub_option == 1:
                for par_numbers in number:
                    if par_numbers % 2 == 0:
                        print(
                            f"Estes são os números pares da lista: {par_numbers}")
            elif sub_option == 2:
                for impar_numbers in number:
                    if impar_numbers % 2 != 0:
                        print(
                            f"Estes são os números impares da lista: {impar_numbers}")

            elif sub_option == 3:
                print("Voltando ao menú principal")
            else:
                err()
    elif option == 4:
        print(f"Saindo do programa...")
        quit()
    else:
        err()
        input("Aperte ENTER para voltar ao menú principal")
