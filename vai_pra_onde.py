opcoes = []
while True:
    destino = input()
    destino = destino.upper()
    if(destino == "FIM"):
        for opcao in opcoes:
            if(opcao[2] * 2 <= 300):
                if(opcao[1] >= maiordistancia):
                    maiordistancia = opcao[1]
                    destinoescolhido = opcao[0]      
                    print(destinoescolhido)
                    break
        else:
            print("SEM DESTINO")
        break
    distancia = int(input())
    passagem = int(input())
    opcoes.append([destino, distancia, passagem])
    maiordistancia = distancia
