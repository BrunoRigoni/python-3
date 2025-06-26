import sqlite3
import os


def clear():
    os.system('cls' if os.name == 'nt' else 'clear')


def pause():
    input("Enter para voltar.")


banco = sqlite3.connect('primeiro_banco.db')


cursor = banco.cursor()

# cursor.execute("CREATE TABLE pessoas (nome text, idade integer, email text)")


def inserir_nova_pessoa():
    nome = input("Nome: ")
    idade = int(input('Idade: '))
    mail = input("Email: ")
    cursor.execute(f"INSERT INTO pessoas VALUES('{nome}',{idade},'{mail}')")
    banco.commit()


while True:
    try:
        option = int(input("[1] Adicionar pessoa.| [2] Sair."))
    except ValueError:
        print("Digite uma opção válida.")
        continue

    if option == 1:
        clear()
        inserir_nova_pessoa()
        pause()
        clear()
    elif option == 2:
        clear()
        print('Saindo...')
        quit()
    else:
        print("Opção inválida.")
        pause()
