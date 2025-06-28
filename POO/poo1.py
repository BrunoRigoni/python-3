class Vendedor():
    def __init__(self, name):
        self.name = name
        self.vendas = 0

    def vendeu(self, vendas):
        self.vendas += vendas

    def bateu_meta(self, meta):
        if self.vendas > meta:
            print(f"{self.name} bateu a meta")
        else:
            print(f"{self.name}não bateu meta")


vendedor1 = Vendedor("Bruno")
vendedor1.vendeu(1000)
vendedor1.bateu_meta(600)

print(vendedor1.vendas, vendedor1.bateu_meta)
