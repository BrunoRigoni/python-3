print("Seja bem vindo ao verificador de números pares")
print("---")
print("---")
print("---")
print("---")
num = input('Digite o número que deseja saber se é par ou impar: ')
num = int(num)

if num % 2 == 0:
    print("------------------------")
    print("O número é par!")
    print("------------------------")
else:
    print("------------------------")
    print("O número é impar!")
    print("------------------------")
