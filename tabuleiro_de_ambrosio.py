
ultima_casa = int(input('Número de casas do tabuleiro: '))
atual = 1
rodada = 0
valores_do_dado = [1,2,3,4,5,6]
while True:
    for valor_dado in valores_do_dado:
        if atual == ultima_casa:
            break
        elif atual > ultima_casa:
            atual = atual - ultima_casa
        atual += valor_dado
        rodada += 1
    print(atual)
    if atual == ultima_casa:
        break
print(rodada)
