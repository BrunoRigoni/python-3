import getpass
import random

users = []
user = {}


id = "id"
name = "name"
password = "password"


def register_new_user():
    new_user_id = random.randint(1, 1000)
    new_user_name = input("Digite o nome de usuario: ")

    print("Digite um valor correto.")

    for user in users:
        if user[name] == new_user_name:
            print("Usuario ja existe.")
        return
    try:
        new_password = getpass.getpass("Digite a senha do usuario: ")
        confirm_password = getpass.getpass("Confirme a senha do usuario: ")
    except Exception as erro:
        print(f"Erro ao capturar senha: {erro}")
        input("ENTER para volar ao menú principal")
        return

    if confirm_password != new_password:
        print("As senhas precisam ser iguais!")
        return

    user = {
        "id": new_user_id,
        "name": new_user_name,
        "password": new_password,
    }

    users.append(user)
    print("Usuario criado com sucesso!")


def show_all_users():
    for show_user in users:
        print(
            f" id: {show_user[id]}\n nome: {show_user[name]}\n senha: {show_user[password]}")


def remove_user():

    try:
        user_remove_id = int(
            input("Digite a ID do usuario que deseja remover:"))
    except ValueError:
        print(f"Erro, por favor digite um número válido.")
        return

    for user in users:
        if user["id"] == user_remove_id:
            users.remove(user)
            print(
                f" O usuario ID: {user_remove_id} foi removido com sucesso.  ")
            return

        print(
            f"O ID: {user_remove_id} não foi encontrado! Digite um ID válido.")


def sep(sepstr):
    print(sepstr * 80)


option = 0

while option != 5:
    sep("*")
    print("BEM VINDO AO CADASTRO DE USUARIOS.")
    sep("")
    sep("")
    sep("-")
    print("[1] CADASTRO DE NOVO USUÁRIO")
    print("[2] CONSULTAR PERFIL")
    print("[3] ALTERAR SENHA")
    print("[4] DELETAR USUARIO")
    print("[5] SAIR")
    sep("-")
    try:
        option = int(input("DIGITE A OPÇÃO QUE DESEJA REALIZAR: "))
    except ValueError:
        sep("*")
        sep("*")
        sep("*")
        print("Não foi possivel obter a opção. Digite apenas números.")
        sep("*")
        sep("*")
        sep("*")
        continue
    sep("")
    if option == 1:
        register_new_user()
        input("ENTER PARA VOLTAR AO MENÚ PRINCIPAL.")
    elif option == 2:
        print("AQUI ESTÁ A LISTA DE USUÁRIOS: ")
        sep("/")
        show_all_users()
        sep("/")
        input("ENTER PARA VOLTAR AO MENÚ PRINCIPAL.")
    elif option == 3:
        print("ALTERAR SENHA")
    elif option == 4:
        remove_user()
        print("CADASTRO DE USUARIO")
    elif option == 5:
        print("APLICAÇÃO ENCERRADA.")

    else:
        print("DIGITE UMA OPÇÃO VÁLIDA!")
        input("ENTER para voltar ao menú principal.")
