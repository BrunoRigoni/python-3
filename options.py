def lines():
    print("*" * 80)


lines()
print("MENU DE INTERAÇÃO COM PYTHON")
lines()

while True:
    print(f"OPTIONS =======================================")
    print("[1]. Mensagem 1")
    print("[2]. Mensagem 2")
    print("[3]. Mensagem 3")
    print("[4]. Sair")
    options = int(input(f"Digite qual opção deseja acessar: "))

    if options == 1:
        while True:
            print("Está é a mensagem 1")
            print("[4]Sair")
            sair = int(input(f"Sair?"))
            if sair == 4:
                break

    elif options == 2:
        while True:
            print("Está é a mensagem 2")
            print("[4]Sair")
            sair = int(input(f"Sair?"))
            if sair == 4:
                break
    elif options == 3:
        while True:
            print("Está é a mensagem 3")
            print("[4]Sair")
            sair = int(input(f"Sair?"))
            if sair == 4:
                break
    else:
        print("Saindo... Até logo!")
        break
