
ano_de_vacinacao = int(input('Ano de vacinação: '))
periodicidade = int(input('Periodicidade (em anos): '))

for doses in range(3):
    print(ano_de_vacinacao+periodicidade)
    ano_de_vacinacao += periodicidade