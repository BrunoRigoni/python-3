def sep():
    print("/" * 80)


produtos = {
    "café": {
        "são joão": 5,
        "brasil": 5,
        "pelé": 3,
        "3 corações": 10,
    },

    "ovos": {
        "granja": 30,
        "caipira": 60,
    },
    "leite": {
        'longa vida': 10,
        'ninho': 10,
        'zero lactose': 5
    },
    "higiene": {
        'antitranspirante masculino': 10,
        'antitranspirante feminino': 10},

    "limpeza": {
        'veja': 10,
        'detergente': 6,
        'sabão em pó': 10
    },
    "padaria": {
        'pão de forma': 10,
        'pão de hot-dog': 10}


}


def mostrar_menu():
    print(f"MENU PRINCIPAL")
    for menu_items, options in menu.items():
        print(f"[{menu_items}], {options}")


def ver_produtos_cadastrados():
    for mostrar_produtos, quantidades in produtos.items():
        print(mostrar_produtos, quantidades)


def cadastrar_produto():
    categoria = input("Digite a categoria do produto: ").strip().lower()
    nome_produto = input(
        "Digite o novo produto que deseja adicionar: ").strip().lower()
    quantidade_produto = int(
        input("Digite a quantidade que deseja adicionar: "))

    if categoria in produtos:
        produtos[categoria][nome_produto] = quantidade_produto
    else:
        produtos[categoria] = {nome_produto: quantidade_produto}

    print(
        f"\nProduto '{nome_produto}' adicionado com sucesso na categoria '{categoria}'!")


def remover_produto():
    ver_produtos_cadastrados()
    categoria = input(
        "Digite qual dos produtos acima produto deseja remover : ").strip().lower()
    if categoria in produtos:
        produto_remover = input("Qual produto deseja remover?").strip().lower()

        if produto_remover in produtos[categoria]:
            del produtos[categoria][produto_remover]
            print(
                f"\nO PRODUTO {produto_remover} foi removido com sucesso da categoria {categoria}")
        if not produtos[categoria]:
            del produtos[categoria]
            print(f"A categoria {categoria} está vazia e foi removida")

        else:
            print("Produto não encontrado")
    else:
        print("Categoria não encontrada.")


menu = {
    1: "VER PRODUTOS CADASTRADOS",
    2: "ADICIONAR PRODUTOS",
    3: "REMOVER PRODUTOS",
    4: "SAIR"
}


while True:
    mostrar_menu()
    try:
        option = int(input("DIGITE A OPÇÃO QUE DESEJA REALIZAR:"))
        if option == 1:
            ver_produtos_cadastrados()
            input("Aperte ENTER para voltar ao menú principal.")
        elif option == 2:
            cadastrar_produto()
            input("Aperte ENTER para voltar ao menú principal.")
        elif option == 3:
            remover_produto()
            input("Aperte ENTER para voltar ao menú principal.")
        elif option == 4:
            print("FINALIZANDO APLICAÇÃO.")
            break
        else:
            input("OPÇÃO INVÁLIDA! APERTE ENTER PARA VOLTAR AO MENU PRINCIPAL")
    except ValueError:
        print("Digite apenas números válidos para as opções")
