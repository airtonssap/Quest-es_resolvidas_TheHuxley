"""
lista1 = list()
lista2 = list()
biblioteca = dict()
foram = int(input('Quantidade de inscritos que se apresentaram a prova: '))

for repeticao in range(foram):
    cpf = int(input(f'CPF do {repeticao+1}º candidato: '))
    lista1.append(cpf)

for indice, valor in enumerate(lista1):
    nota = int(input(f'Nota do {indice+1}º candidato: '))
    biblioteca[valor] = nota

pesquisa = int(input('Quantidade de casos que serão pesquisados: '))

for repeticao3 in range(pesquisa):
    cpf = int(input('CPF do candidato a ser pesquisado a nota: '))
    lista2.append(cpf)

for valor in lista2:
    if valor in biblioteca.keys():
        print(biblioteca[valor])
    else:
        print('NAO SE APRESENTOU')
"""
"""
lista1 = list()
lista2 = list()
lista3 = list()
foram = int(input('Quantidade de inscritos que se apresentaram a prova: '))

for repeticao in range(foram):
    cpf = int(input(f'CPF do {repeticao+1}º candidato: '))
    lista1.append(cpf)

for repeticao2 in range(foram):
    nota = int(input(f'Nota do {repeticao2+1}º candidato: '))
    lista2.append(nota)

pesquisa = int(input('Quantidade de casos que serão pesquisados: '))

for repeticao3 in range(pesquisa):
    cpf = int(input('CPF do candidato a ser pesquisado a nota: '))
    lista3.append(cpf)

for valor in lista3:
    if valor in lista1:
        indice = lista1.index(valor)
        print(lista2[indice])
    else:
        print('NAO SE APRESENTOU')
"""

listacpf = list()
listacpfnota = list()
listacpfprocura = list()

foram = int(input('Quantidade de inscritos que se apresentaram a prova: '))

for repeticao in range(foram):
    cpf = int(input(f'CPF do {repeticao+1}º candidato: '))
    listacpf.append(cpf)
    
for repeticao2 in range(foram):
    nota = int(input(f'Nota do {repeticao2+1}º candidato: '))
    listacpfnota.append([listacpf.copy()[repeticao2], nota])

listacpfnota = sorted(listacpfnota)
pesquisa = int(input('Quantidade de casos que serão pesquisados: '))

for repeticao3 in range(pesquisa):
    cpf = int(input('CPF do candidato a ser pesquisado a nota: '))
    listacpfprocura.append(cpf)

for valor in listacpfprocura:
    menor = 0
    maior = len(listacpfnota)-1
    while menor <= maior:
        central = round((menor + maior)/2)
        if valor == listacpfnota[central][0]:
            print(listacpfnota[central][1])
            break
        if listacpfnota[central][0] > valor:
            maior = central-1
        else:
            menor = central+1
    if valor != listacpfnota[central][0]:
        print('NAO SE APRESENTOU')
