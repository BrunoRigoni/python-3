produto = input("Qual produto deseja calcular o desconto? : ")
preco = float(input("Qual o preço do produto : ").replace(",", "."))
preco = round(preco, 2)


print("------------------------------------------------------------")
print(f"O produto {produto} está custando {preco} R$".replace(".", ","))
print("------------------------------------------------------------")

print("------------------------------------------------------------")
desconto = float(
    input("Quantos porcento será aplicado de desconto? ").replace(",", "."))
desconto = round(desconto, 2)
print("------------------------------------------------------------")
print("------------------------------------------------------------")
if desconto == 0:
    print("Descontos zerados não podem ser aplicados!")
elif desconto > 50:
    print(f"Erro, Desconto muito alto e fora dos padrões! ")
else:

    calc_desconto = (desconto / 100)
    valor_desconto = (preco * calc_desconto)
    valor_desconto = round(valor_desconto, 2)

    print(f"O valor total do desconto será de: {valor_desconto} R$ ".replace(
        ".", ","))

    valor_final = float(preco - valor_desconto)
    valor_final = round(valor_final, 2)
    print(f"O valor final da compra é de : {valor_final} R$".replace(".", ","))
