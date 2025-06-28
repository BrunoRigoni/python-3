import random

users = []


class User:
    def __init__(self, name, mail):
        self.id = random.randint(100, 300)
        self.name = name.strip().title()
        self.mail = mail.strip().lower()

    def show_user(self):
        print(f"ID: {self.id} | Nome: {self.name} | Email: {self.mail}")


while True:
    try:
        option = int(
            input("\n[1] CADASTRAR USUÁRIO | [2] LISTAR USUÁRIOS | [3] SAIR\nEscolha: "))
    except ValueError:
        print("Digite uma opção válida.")
        continue

    if option == 1:
        name = input("Nome do usuário: ")
        mail = input("Email do usuário: ")
        new_user = User(name, mail)
        users.append(new_user)
        print("\n✅ Usuário cadastrado:")
        new_user.show_user()
        input("ENTER para continuar...")

    elif option == 2:
        if not users:
            print("Nenhum usuário cadastrado.")
        else:
            print("\n👤 Lista de Usuários:")
            for user in users:
                user.show_user()
        input("ENTER para continuar...")

    elif option == 3:
        print("Saindo...")
        break

    else:
        print("Opção inválida.")
        input("ENTER para continuar...")
