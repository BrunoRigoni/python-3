def separador():
    print("-" * 80)


separador()
print("Bem vindo a calculadora de IMC, digite as informações a baixo: ")
separador()

nome_usuario = input("Digite seu nome: ")
separador()

peso_pessoa = float(input("Digite seu peso :").replace(",", "."))
peso_pessoa = round(peso_pessoa, 2)


separador()

altura_pessoa = float(input("Digite sua altura :").replace(",", "."))
altura_pessoa = round(altura_pessoa, 2)

if peso_pessoa <= 0 or altura_pessoa <= 0:
    print("Peso e altura inválidos. Devem ser maiores que zero.")
    exit()


imc_usuario = peso_pessoa / altura_pessoa ** 2
imc_usuario = round(imc_usuario, 2)


separador()
print("")
print("")

if imc_usuario <= 18.5:
    print("")
    separador()
    print(f"O usuario {nome_usuario} está pesando {str(peso_pessoa).replace(".", ",")}kg e tem {altura_pessoa} de altura. Seu IMC (Índice de Massa Corporal) é de {str(imc_usuario).replace(".", ",")}. O IMC de {imc_usuario} significa que está a baixo do peso!")
    separador()
    print(" ")
    print(" ")
elif imc_usuario <= 24.9:
    print("")
    separador()
    print(f"O usuario {nome_usuario} está pesando {str(peso_pessoa).replace(".", ",")}kg e tem {altura_pessoa} de altura. Seu IMC (Índice de Massa Corporal) é de {imc_usuario}. O IMC de {str(imc_usuario).replace(".", ",")} significa que você está no peso normal!")
    print("----------------------------------------------------------------------------------------------")
    print(" ")
    print(" ")
elif imc_usuario <= 29.9:
    print(" ")
    separador()
    print(f"O usuario {nome_usuario} está pesando {str(peso_pessoa).replace(".", ",")}kg e tem {altura_pessoa} de altura. Seu IMC (Índice de Massa Corporal) é de {imc_usuario}. O IMC de {str(imc_usuario).replace(".", ",")} significa que você está com sobrepeso!".replace(".", ","))
    separador()
    print(" ")
    print(" ")
elif imc_usuario <= 34.9:
    print("")
    separador()
    print(
        f"O usuario {nome_usuario} está pesando {str(peso_pessoa).replace(".", ",")}kg e tem {altura_pessoa} de altura. Seu IMC (Índice de Massa Corporal) é de {imc_usuario}. O IMC de {str(imc_usuario).replace(".", ",")} significa que você está com obesidade grau 1! Procure um médico!")
    separador()
    print(" ")
    print(" ")
elif imc_usuario <= 39.9:
    print("")
    separador()
    print(
        f"O usuario {nome_usuario} está pesando {str(peso_pessoa).replace(".", ",")}kg e tem {altura_pessoa}m de altura. Seu IMC (Índice de Massa Corporal) é de {imc_usuario}. O IMC de {str(imc_usuario).replace(".", ",")} significa que você está com obesidade grau 2! Procure um médico!")
    separador()
    print(" ")
    print(" ")
else:
    print("")
    separador()
    print(
        f"O usuario {nome_usuario} está pesando {str(peso_pessoa).replace(".", ",")}kg e tem {altura_pessoa}m de altura. Seu IMC (Índice de Massa Corporal) é de {imc_usuario}. O IMC de {str(imc_usuario).replace(".", ",")} significa que você está com obesidade grau 3! Procure um médico!")
    separador()
    print(" ")
    print(" ")
