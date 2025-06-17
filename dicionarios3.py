mochila = {
    "garrafa": "agua",
    "estojo": "lapis",
}
# dicionário criado

# visualizando os itens e valores dentro da mochila
print(mochila)  # de forma crua:


def ver_todos_itens():
    for itens, conteudo in mochila.items():
        print(f"itens: {itens} -> {conteudo}")
# visualizando de uma forma mais amigavel:


def ver_item_simples():
    # criando a váriavel que recebe o valor digitado
    item_mochila = input("Digite o item da mochila que deseja ver: ")
    # usando a váriavel para ver o valor/ dentro do dicionário.
    print(f"{mochila[item_mochila]}")


def adicionar_novo_item():
    # adicionando um novo item com um novo valor:
    novo_item = input("Digite o item que deseja adicionar: ")
# ex garrafa
    novo_conteudo = input("Digite o conteudo do novo item: ")
    mochila[novo_item] = novo_conteudo
    print(f"{novo_conteudo} foi adicionado com sucesso.")


def remover_itens():
    remover_item = input("Digite o item que deseja remover: ")
    mochila.pop(remover_item)
    print(f"O item: {remover_item} foi removido com sucesso!")


def atualizar_itens():
    atualizar_item = input("Digite qual item deseja atualizar o valor: ")
    atualizar_valor = input("Digite o novo valor: ")
    mochila[atualizar_item] = atualizar_valor
    print(
        f"O item: {atualizar_item} foi atualizado com sucesso para o valor: {atualizar_valor}!")


while True:
    print("[1] - VER TODOS OS ITENS")
    print("[2] - VER ITEM ESPECIFICO")
    print("[3] - ADICIONAR NOVO ITEM")
    print("[4] - REMOVER ITEM")
    print("[5] - ATUALIZAR ITEM")
    print("[6] - SAIR")

    opcao = int(input("DIGITE A OPÇÃO QUE DESEJA REALIZAR: "))

    if opcao == 1:
        ver_todos_itens()
        input("Aperte ENTER para voltar ao menú principal...")
    elif opcao == 2:
        ver_item_simples()
        input("Aperte ENTER para voltar ao menú principal...")

    elif opcao == 3:
        adicionar_novo_item()
        input("Aperte ENTER para voltar ao menú principal...")
    elif opcao == 4:
        remover_itens()
        input("Aperte ENTER para voltar ao menú principal...")

    elif opcao == 5:
        atualizar_itens()
        input("Aperte ENTER para voltar ao menú principal...")
    elif opcao == 6:
        print("Encerrando...")
        break
    else:
        print("Digite uma opção válida.")
        input("Aperte ENTER para voltar ao menú principal...")
