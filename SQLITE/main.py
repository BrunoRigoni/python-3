from usuarios import criar_tabela, cadastrar_usuario, listar_nomes


criar_tabela()

while True:

    try:
        option = int(
            input("[1] Para adicionar. nomes [2] Para listar nomes. [3] Para sair."))
    except ValueError:
        print("Digite uma opção válida.")
        continue

    if option == 1:
        nome = input("DIGITE O NOME QUE DESEJA ADICIONAR: ")

        if nome.strip():
            cadastrar_usuario(nome)
        else:
            print("Nome inválido. Tente novamente.")
    elif option == 2:
        listar_nomes()
    elif option == 3:
        quit()
    else:
        print("DIGITE UMA OPÇÃO VÁLIDA.")
