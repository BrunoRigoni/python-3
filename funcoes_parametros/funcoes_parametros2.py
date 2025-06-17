def calc_media(n1, n2, n3):
    sum_notas = n1 + n2 + n3
    media = sum_notas / 3
    media = round(media, 2)
    return media


nome_aluno = input("Digite o nome do aluno").capitalize()
nota_1 = float(input("Digite a primeira nota: "))
nota_2 = float(input("Digite a segunda nota: "))
nota_3 = float(input("Digite a terceira nota: "))


print(
    f"A média de notas do aluno {nome_aluno} foi de: {calc_media(nota_1, nota_2, nota_3)}")
