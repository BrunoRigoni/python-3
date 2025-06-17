def mostrar_itens(dic):

    for chaves, valor in dic.items():
        print(f"Chaves: {chaves} - Valor: {valor}")


mochila = {
    "caderno": "historia",
    "garrafa": "agua",
}

mostrar_itens(mochila)


def atualizar_itens(dic, chaves, valor):
    dic[chaves] = valor
    print(f"O item {chaves} foi adicionado com o valor {valor}...")


novo_item = input("DIGITE O ITEM QUE DESEJA ATUALIZAR: ")
novo_valor = input("DIGITE O VALOR DO ITEM QUE DESEJA ATUALIZAR: ")

atualizar_itens(mochila, novo_item, novo_valor)
