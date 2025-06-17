def sep():
    print("=" * 80)


estoque = ["leite", "ovos", "pão", "queijo", "presunto", "requeijao",]
option = 0


def mostrar_produto():
    for produtos in estoque:
        print(f" - {produtos} ")


while True:
    sep()
    sep()
    print("Bem vindo ao Controle de Estoque")
    print("[1] - Adicionar produto")
    print("[2] - Remover produto")
    print("[3] - Listar produtos")
    print("[4] - Sair")
    option = int(input("DIGITE A OPÇÃO QUE DESEJA REALIZAR: "))

    if option == 1:

        novo_produto = input(
            "Digite o produto que deseja adicionar: ").strip().lower()
        estoque.append(novo_produto)
        print(f"O produto '{novo_produto}' foi adicionado com sucesso!")

    elif option == 2:
        remover_produto = input(
            "DIGITE O PRODUTO QUE DESEJA REMOVER: ").strip().lower()
        if remover_produto in estoque:
            estoque.remove(remover_produto)
            print(f"O produto {remover_produto} foi removido com sucesso!")
        else:
            print(
                f"Produto {remover_produto} não existe no estoque, digite um produto válido.")

    elif option == 3:
        mostrar_produto()
        input("Aperte ENTER para voltar ao menú principal")

    elif option == 4:
        print("SAINDO DO ESTOQUE...")
        break

    else:
        print("Opção inválida!")
