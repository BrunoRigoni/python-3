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


show_all_users()


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


remove_user()

show_all_users()
