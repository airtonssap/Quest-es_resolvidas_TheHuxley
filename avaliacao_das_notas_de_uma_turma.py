
biblioteca = dict()
while True:
    aluno_nota = input('Primeiro nome e nota do aluno: ')
    if aluno_nota == '*':
        break
    aluno_nota = aluno_nota.split()
    aluno, nota = aluno_nota[0], aluno_nota[1]
    biblioteca[aluno] = nota


gabarito = input('Gabarito oficial: ')
lista = []
nota = 0
for valor in biblioteca.values():
    for iteravel in range(len(valor)):
        if valor[iteravel] == gabarito[iteravel]:
            nota += 1
    lista.append(nota)
    nota = 0

print(f'Maior: {max(lista)}')
print(f'Menor: {min(lista)}')
print(f'Media: {sum(lista)/len(lista):.2f}')