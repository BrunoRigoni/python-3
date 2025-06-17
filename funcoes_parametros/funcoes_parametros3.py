

def saudacao(nome, horario):
    if horario >= 6 and horario < 12:
        msg = "bom dia"
    elif horario >= 12 and horario < 18:
        msg = "boa tarde"
    elif horario >= 18 and horario < 24:
        msg = "boa noite"
    elif horario > 0 and horario < 6:
        msg = "boa madrugada"
    else:
        msg = "horario desconhecido"
    return print(f"Olá, {nome}! Tenha uma {msg}")


nome_usuario = input("DIGITE SEU NOME: ")
horario_login = float(input("DIGITE O HORARIO ATUAL DE LOGIN"))

saudacao(nome_usuario, horario_login)
