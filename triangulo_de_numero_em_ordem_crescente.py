
repeticao = int(input('Digite um valor x, tal que 1 <= x <= 30: '))
inicio = 1

for impressao in range(1, repeticao+1):
    print(str(inicio)*impressao)
    inicio += 1
