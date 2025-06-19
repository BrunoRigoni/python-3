import getpass
import random


users = []
user = {}


id = "id"
name = "name"
password = "password"


def sing_in():
    new_user_id = random.randint(1, 1000)
    new_user_name = input("Digite seu nome: ")

    for user in users:
        if user['name'] == new_user_name:
            print("Usuario ja existe.")
            return

    new_password = getpass.getpass("Digite sua senha: ")
    confirm_password = getpass.getpass("Confirme sua senha: ")

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


sing_in()
sing_in()
sing_in()


def show_all_users():
    for show_user in users:
        print(
            f"AQUI ESTÁ A LISTA DE USUÁRIOS:\n{"-" * 80}\n id: {show_user[id]}\n nome: {show_user[name]}\n senha: {show_user[password]}\n{"*" * 80}\n")


def remove_user():
    for user in users:
        print(f"ID: {user["id"]} -> nome: {user["name"]}")

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


remove_user()

show_all_users()


def new_password():
    try:
        user_id = int(
            input("Digite o ID do usuario que deseja alterar a senha: "))
    except ValueError:
        print("Digite um número válido.")
        return
    for user in users:
        if user["id"] == user_id:
            try:
                new_pass = getpass.getpass("Digite a nova senha: ")
                new_pass_confirm = getpass.getpass("Confirme a nova senha: ")
            except Exception as erro:
                print(f"Erro ao capturar uma nova senha: {erro}")
                input("ENTER para volar ao menú principal")
                return

            if new_pass == new_pass_confirm:
                user["password"] = new_pass
                print(f"Senha alterada com sucesso.")
            else:
                print("As senhas devem corresponder")
                return


new_password()
