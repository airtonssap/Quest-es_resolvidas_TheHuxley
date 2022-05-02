
qnt_arvores_e_madeira = input('Quantidade de árvore e madeira necessária: ').split()
arvores = sorted(input('Altura das árvores: ').split())
max_posicao = len(arvores)-1
corte = 0

while corte < int(qnt_arvores_e_madeira[1]):
    maximo = int(arvores[max_posicao])-1
    arvores[max_posicao] = str(maximo)
    arvores = sorted(arvores)
    corte += 1

print(arvores[max_posicao])
