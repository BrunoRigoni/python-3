def operacoes(a, b):
    soma = a + b
    sub = a - b
    multiplicacao = a * b
    return print(f"A soma é: {soma}, a subtração é: {sub} e a multiplicação é: {multiplicacao}")


num1 = int(input("DIGITE O PRIMEIRO NÚMERO: "))
num2 = int(input("DIGITE O SEGUNDO NÚMERO: "))

operacoes(num1, num2)
