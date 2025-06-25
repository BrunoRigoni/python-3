import getpass


input_password = getpass.getpass("Digite a senha: ")
confirm_password = getpass.getpass("Confirme a senha: ")


def password(input_password, confirm_password):
    if input_password == confirm_password:
        user_password = input_password
        print(f"Senha definida com sucesso.")
        return user_password
    else:
        print("As senhas devem coincidir.")


password(input_password, confirm_password)


def mail(input_mail, confirm_mail):
    if input_mail == confirm_mail:
