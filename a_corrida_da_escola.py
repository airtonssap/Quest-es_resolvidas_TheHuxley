
competidores_e_voltas = input('Digite o número de competidores e o número de voltas: ').split()
temposdoscompetidores = []
soma = 0
melhortempo = 1000000
for competidor in range(1,int(competidores_e_voltas[0])+1):
    tempodocompetidor = input(f'Tempo do {competidor}º competidor: ').split()
    for valores in tempodocompetidor:
        soma += int(valores)
    if soma < melhortempo:
        melhortempo = soma
        melhorcompetidor = competidor
    soma = 0

print(melhorcompetidor)
