import getpass
import random
import os
import json

users = []
DATA_FILE = 'users.json'

id = "id"
name = "name"
password = "password"


def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')


def save_users():
    with open(DATA_FILE, 'w') as file:
        json.dump(users, file, indent=4)


def load_users():
    global users
    try:
        with open(DATA_FILE, 'r') as file:
            users = json.load(file)
    except FileNotFoundError:
        users = []


def register_new_user():
    new_user_id = random.randint(1, 1000)
    new_user_name = input("Digite o nome de usuario: ")

    for user in users:
        if user["name"] == new_user_name:
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
    save_users()
    print("Usuario criado com sucesso!")


def show_all_users():
    for show_user in users:
        print(
            f" id: {show_user[id]}\n nome: {show_user[name]}\n senha: ****")


def new_password():
    for user in users:
        print(f"ID: {user["id"]} -> nome: {user["name"]}")
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
                save_users()
                print(f"Senha alterada com sucesso.")
            else:
                print("As senhas devem corresponder")
            return
    print("ID não encontrado! ")


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
            save_users()
            print(
                f" O usuario ID: {user_remove_id} foi removido com sucesso.  ")
            return

    print(
        f"O ID: {user_remove_id} não foi encontrado! Digite um ID válido.")


def sep(sepstr):
    print(sepstr * 80)


option = 0
load_users()

while option != 5:
    sep("*")
    print("BEM VINDO AO CADASTRO DE USUARIOS.")
    sep("")
    sep("")
    sep("-")
    print("[1] CADASTRO DE NOVO USUÁRIO")
    print("[2] CONSULTAR CADASTROS")
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
        clear_screen()
    elif option == 2:
        print("AQUI ESTÁ A LISTA DE USUÁRIOS: ")
        sep("/")
        show_all_users()
        sep("/")
        input("ENTER PARA VOLTAR AO MENÚ PRINCIPAL.")
        clear_screen()
    elif option == 3:
        new_password()
        input("ENTER PARA VOLTAR AO MENÚ PRINCIPAL.")
        clear_screen()
    elif option == 4:
        remove_user()
        input("ENTER PARA VOLTAR AO MENÚ PRINCIPAL.")
        clear_screen()
    elif option == 5:
        print("APLICAÇÃO ENCERRADA.")
        quit()

    else:
        print("DIGITE UMA OPÇÃO VÁLIDA!")
        input("ENTER para voltar ao menú principal.")
        clear_screen()
