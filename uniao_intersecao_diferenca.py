
vetor1 = int(input('Digite a quantidade de elementos do primeiro vetor: '))
vetor2 = int(input('Digite a quantidade de elementos do segundo vetor: '))

lista1 = []
lista2 = []
listaintersecao = []
listadiferenca = []
listauniao = []

for repeticao1 in range(1,vetor1 + 1):
    elementode1 = input(f'{repeticao1}º valor: ')
    lista1.append(elementode1)

for repeticao2 in range(1, vetor2 + 1):
    elementode2 = input(f'{repeticao2}º valor: ')
    lista2.append(elementode2)
    if elementode2 in lista1:
        listaintersecao.append(elementode2)

for valores2 in lista2:
    listauniao.append(valores2)

for valores1 in lista1:
    if valores1 not in lista2:
        listadiferenca.append(valores1)
        listauniao.append(valores1)

print(listauniao)
print(listaintersecao)
print(listadiferenca)