casa = {
    "pessoa1": "Bruno",
    "pessoa2": "Emily"
}

print(casa["pessoa1"])

if "pessoa3" in casa:
    print(casa["pessoa3"])
else:
    print("pessoa3 não existe ainda dentro da casa!")
    print("Deseja adicionar uma nova pessoa a esta casa?")
    print("[1] para adicionar//[2]Para não adicionar")

    opção = int(input("Digite qual opção deseja:"))

    if opção == 1:
        nova_pessoa = input("Digite o nome da pessoa que deseja adicionar")
        casa["pessoa3"] = nova_pessoa
        for residencia, pessoas in casa.items():
            print(residencia, pessoas)
    elif opção == 2:
        quit()
    else:
        print("opção inválida.")
