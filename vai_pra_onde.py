lista_de_cidades = []
lista = []
while True:
    cidade = input('Digite a cidade: ')
    if cidade == 'Fim':
        break
    dis = float(input(f'Digite a distância de {cidade} até o seu local atual: '))
    valor = float(input('Valor da passagem: ')) * 2
    if valor > 300:
        continue
    lista.append(cidade)
    lista.append(dis)
    lista.append(valor)
    lista_de_cidades.append(lista.copy())
    lista.clear()

Escolhida = ''
maiordis = 0
if len(lista_de_cidades) > 0:
    for valor in lista_de_cidades:
        if valor[1] > maiordis:
            maiordis = valor[1]
            Escolhida = valor[0].upper()
    print(Escolhida)
else:
    print('SEM DESTINO')
    