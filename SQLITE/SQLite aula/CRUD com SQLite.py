import sqlite3
import os


def clear():
    os.system('cls' if os.name == 'nt' else 'clear')


def pause():
    input("Enter para voltar.")


banco = sqlite3.connect('primeiro_banco.db')


cursor = banco.cursor()


def criar_tabela():
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS pessoas (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nome TEXT,
        idade INTEGER,
        email TEXT
    )
    """)
    banco.commit()


def inserir_nova_pessoa():
    try:
        nome = input("Nome: ").strip()
        idade = int(input('Idade: '))
        mail = input("Email: ").strip()
        cursor.execute(
            "INSERT INTO pessoas (nome, idade, email) VALUES (?, ?, ?)",
            (nome, idade, mail)
        )
        banco.commit()
        print("Usuário adicionado com sucesso!")
    except ValueError:
        print("Idade deve ser um número inteiro.")
    except sqlite3.Error as error:
        print(f"\nErro ao adicionar usuário: {error}")


def deletar_pessoa_por_id():
    try:
        user_id = int(input("Digite o ID do usuário que deseja excluir: "))
        cursor.execute("DELETE FROM pessoas WHERE id = ?", (user_id,))
        banco.commit()
        print(f"Usuário com ID {user_id} -> removido com sucesso.")
    except ValueError:
        print("Por favor, digite um número inteiro válido.")
    except sqlite3.Error as erro:
        print(f"\nErro ao excluir usuário: {erro}")


def atualizar_email():
    try:
        main_email = input("Email que deseja alterar:").strip()
        update_mail = input('Novo email ').strip()
        banco.execute("UPDATE pessoas SET email = ? WHERE email = ?", (
            update_mail, main_email))
        banco.commit()
    except sqlite3.Error as error:
        print(f"O email inicial precisa ser válido. {error} ")


def atualizar_idade():
    try:
        main_email = input("Digite o email para atualizar a idade: ").strip()
        update_idade = int(input('Nova idade: '))
        banco.execute("UPDATE pessoas SET idade = ? WHERE email = ?",
                      (update_idade, main_email))
        banco.commit()
    except ValueError:
        print("Idade precisa ser válida.")
    except sqlite3.Error as erro:
        print(f'Erro ao atualizar idade: {erro}')


while True:
    try:
        option = int(
            input("[1] Criar tabela. | [2] Adicionar pessoa. | [3] Remover pessoa. | [4] Atualizar usuário. | [5] Sair. \n \n [Opção] = "))
    except ValueError:
        print("Digite uma opção válida.")
        continue
    if option == 1:
        clear()
        criar_tabela()
        print("TABELA CRIADA!")
    elif option == 2:
        clear()
        inserir_nova_pessoa()
        pause()
        clear()
    elif option == 3:
        clear()
        deletar_pessoa_por_id()
        pause()
        clear()
    elif option == 4:
        while True:
            try:
                user_option = int(
                    input("[1] Atualizar email. | [2] Atualizar idade. | [3] Sair. \n \n[Opção] = "))
            except ValueError:
                continue
            if user_option == 1:
                clear()
                atualizar_email()
                pause()
                clear()
            elif user_option == 2:
                clear()
                atualizar_idade()
                pause()
                clear()
            elif user_option == 3:
                clear()
                print("Voltando...")
                break

    elif option == 5:
        clear()
        print('Saindo...')
        quit()
    else:
        print("Opção inválida.")
        pause()
