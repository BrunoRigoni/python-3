tarefas = [
    {"titulo": "Estudar Python", "concluida": False},
    {"titulo": "Estudar CRUD", "concluida": False},
    {"titulo": "EMILY", "concluida": False},
    {"titulo": "valorant", "concluida": False},
    {"titulo": "mysql", "concluida": False},
    {"titulo": "sqlite", "concluida": False},
]


# Adicionar tarefas
def adicionar_tarefas():
    while True:
        try:
            option = int(
                input("[0]Para continuar adicionando tarefas [1]Para sair]"))
        except ValueError:
            print("Digite um número válido.")
            return

        if option == 0:
            titulo_tarefa = input("Digite a nova tarefa: ")

            nova_tarefa = {
                "titulo": titulo_tarefa,
                "concluida": False,
            }
            tarefas.append(nova_tarefa)
            print(tarefas)

        elif option == 1:
            input("ENTER para parar.")
            break
        else:
            print("Digite uma opção válida.")
            return

# Listar tarefas


def mostrar_tarefas():
    for i, tarefa in enumerate(tarefas):
        print(i, tarefa['titulo'], tarefa['concluida'])

# Marcar tarefas como concluídas


def concluir_tarefas():
    print("x" * 80)
    mostrar_tarefas()
    tarefa_concluir = input("Digite a tarefa que deseja concluir: ")
    for tarefa in tarefas:
        if tarefa['titulo'] == tarefa_concluir:
            tarefa['concluida'] = True
            print(tarefa['titulo'], tarefa['concluida'])
            return

# Excluir tarefas


def excluir_tarefas():
    mostrar_tarefas()

    tarefa_excluir = input("Digite a tarefa que deseja excluir: ")
    for tarefa in tarefas:
        if tarefa['titulo'] == tarefa_excluir:
            tarefas.remove(tarefa)
            print(f'Tarefa: {tarefa_excluir} foi removido com sucesso.')
            return


while True:
    print("[1] -> Adicionar Tarefas ")
    print("[2] -> Remover Tarefas ")
    print("[3] -> Mostrar Tarefas ")
    print("[4] -> Concluir Tarefas ")
    print("[5] -> Sair ")
    try:
        option = int(input("[DIGITE A OPÇÃO QUE DESEJA REALIZAR.]"))
    except ValueError:
        print("Digite uma opção válida.")

    if option == 1:
        print("-> Adicionar Tarefas ")
        adicionar_tarefas()
    elif option == 2:
        print("-> Remover Tarefas ")
        excluir_tarefas()
    elif option == 3:
        print("-> Mostrar Tarefas ")
        mostrar_tarefas()
    elif option == 4:
        print("-> Concluir Tarefas ")
        concluir_tarefas()

    elif option == 5:
        print("SAINDO... ")
        break
    else:
        print('DIGITE UMA OPÇÃO VÁLIDA.')
