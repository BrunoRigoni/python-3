estoque = ["uva", "pera", "maçã", "abacaxi",]


cliente = {}
cliente["nome"] = "Bruno"
cliente["idade"] = "24"
cliente["estoque"] = estoque
cliente["id"] = 1

print(cliente)

cliente["nacionalidade"] = "brasileiro"
print(cliente)
estoque.append("pêra")
print(cliente)

for i in estoque:
    print(i)

print(cliente)
