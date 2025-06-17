num1 = 0

num2 = int(input("Até qual número deseja contar?"))


while num1 <= num2:

    if num1 % 2 == 0:
        print(f"Números pares de 0 a {num2} = {num1}")

    num1 += 2
