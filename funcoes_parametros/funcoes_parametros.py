user_name = input("QUAL SEU NOME?")


def apresentar_pessoa(nome):
    print(f"Olá, {nome}! Seja bem vindo!")


apresentar_pessoa(user_name)


def resultado(a, b):
    print(f"A soma de {a} + {b} é igual a = [{a + b}]")


resultado(1, 3)

horario = int(input("QUE HORAS SÃO AGORA? : "))


def mensagem_personalizada(nome, hora):
    if hora < 12 and hora > 6:
        hora = "dia"
        print(f"Olá {nome}, tenha um bom {hora}!")
    elif hora >= 12 and hora < 18:
        hora = "tarde"
        print(f"Olá {nome}, tenha uma boa {hora}")
    elif hora >= 18 and hora < 24:
        hora = "noite"
        print(f"Olá {nome}, tenha uma boa {hora}")
    else:
        hora = "madrugada"
        print(f"Olá {nome}, tenha uma boa {hora}")


mensagem_personalizada(user_name, horario)
