pessoas = [
    {"nome": "Bruno", "idade": 24},
    {"nome": "Emily", "idade": 22},
    {"nome": "Carlos", "idade": 30}
]

idade = "idade"
nome = "nome"


def mostrar_pessoas():
    for pessoa in pessoas:
        print(f"Nome: {pessoa[nome]}, Idade: {pessoa[idade]}")


def nova_pessoa(nome_novo, nova_idade):
    pessoa_nova = {nome: nome_novo, idade: nova_idade}
    pessoas.append(pessoa_nova)
    print(pessoas)


def buscar_nome():
    nome_buscar = input("Digite o nome que deseja buscar: ").lower()
    encontrado = False
    for pessoa in pessoas:
        if pessoa[nome].lower() == nome_buscar.lower():
            print(f"Pessoa encontrada: {pessoa[nome]}")
            encontrado = True
            break

    if not encontrado:
        print("Pessoa não encontrada.")


def atualizar_idade():
    nome_pessoa = input(
        "Digite o nome da pessoa que deseja atualizar a idade: ")

    pessoa_encontrada = False
    for pessoa in pessoas:
        if pessoa[nome].lower() == nome_pessoa.lower():
            idade_atual = pessoa[idade]
            nova_idade = int(input("Digite a nova idade: "))
            pessoa[idade] = nova_idade
            print(
                f"A idade de {pessoa[nome]} foi atualizado de {idade_atual} para {pessoa[idade]} anos.")
            pessoa_encontrada = True
            break
    if not pessoa_encontrada:
        print("Pessoa não encontrada.")


def remover_pessoa():
    pessoa_remover = input("Digite o nome da pessoa que deseja remover: ")
    pessoa_encontrada = False

    for pessoa in pessoas:
        if pessoa[nome].lower() == pessoa_remover.lower():
            pessoas.remove(pessoa)
            print(
                f"A pessoa {pessoa_remover} foi removida da lista com sucesso.")
            mostrar_pessoas()

            pessoa_encontrada = True

            break
    if not pessoa_encontrada:
        print(f"{pessoa_remover} não foi encontrado.")


nova_pessoa("Daniele", 47)
buscar_nome()
atualizar_idade()
remover_pessoa()
