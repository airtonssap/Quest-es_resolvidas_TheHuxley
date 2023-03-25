ano_de_vacinacao = int(input())
periodicidade = int(input())
palavra = ""

for dose in range(3):
    proximo = ano_de_vacinacao + periodicidade
    ano_de_vacinacao += periodicidade
    if dose == 0:
        palavra += str(proximo)
    else:
        palavra += " " + str(proximo)
print(palavra)
