# calculadora simples

print('Bem vindo a Calculadora python!')
name = input("Antes de calcular, nos diga qual o seu nome : ")
print(f"Certo {name}, Vamos aos calculos")


num1 = input('Digite o primeiro número que deseja calcular :')
num2 = input("Agora, digite o segundo número que deseja calcular :")
num1 = int(num1)
num2 = int(num2)


print("Agora, digite qual operação deseja realizar: ")
print("Opçao [1] = +")
print("Opçao [2] = -")
print("Opçao [3] = x")
print("Opçao [4] = ÷")
operador = input("Digite qual operação deseja realizar: ")

if operador == "1":
    print(f"O resultado da soma é : {num1 + num2}")
elif operador == "2":
    print(f"O resultado da subtração é : {num1 - num2}")
elif operador == "3":
    if num1 == 0 or num2 == 0:
        print("Erro, o número não pode ser multiplicado por 0!")
    else:
        print(f"O resultado da multiplicação é: {num1 * num2}")
elif operador == "4":
    if num1 == 0 or num2 == 0:
        print("Erro, o número não pode ser dividido por 0!")
    else:
        print(f"O resultado da divisão é: {float(num1 / num2)}")
else:
    print("Numero incorreto!")
