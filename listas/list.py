def sep():
    print("*" * 80)


produto = ["bolacha", "refrigerante", "café", "oleo"]


for items in produto:
    print(items)

sep()


novo_produto = input("Digite um novo produto: ")

produto.append(novo_produto)

for items in produto:
    print(items)

sep()

remover_produto = input("Digite o produto que deseja remover: ")


if remover_produto in produto:
    produto.remove(remover_produto)
    print(f"O produto: {remover_produto} foi removido com sucesso! ")

else:
    print("Erro")


for items in produto:

    print(items)
