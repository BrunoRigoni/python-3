print("-------------------------------------")
print("Está aplicação dirá se o número digitado é positivo, negativo, impar ou par! Bora tentar? ")
print("-------------------------------------")

num = int(input("Digite qualquer número : "))


if num % 2 == 0 and num < 0:  # verifica se o número é par e negativo
    print("-------------------------------------")
    print(f"O número {num} é negativo e par ")
    print("-------------------------------------")
elif num % 2 != 0 and num < 0:  # verifica se o número é impar e negativo
    print("-------------------------------------")
    print(f"o numero {num} é negativo e impar ")
    print("-------------------------------------")
elif num % 2 == 0 and num > 0:
    print("-------------------------------------")
    print(f"O número {num} é positivo e par ")  # verifica se o número é par
    print("-------------------------------------")
elif num % 2 != 0 and num > 0:
    print("-------------------------------------")
    # verifica se o número é impar
    print(f"O número {num} é positivo e impar ")
    print("-------------------------------------")
elif num % 2 == 0:  # regra para o número zero
    print("-------------------------------------")
    print(f"O número {num} é par ")
    print("-------------------------------------")
