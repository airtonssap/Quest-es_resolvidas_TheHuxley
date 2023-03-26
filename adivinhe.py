
qnt_de_jogos = int(input())

for jogos in range(qnt_de_jogos):
    tam_senha = input()
    senha = input()
    while True:
        tentativa = input()
        if tentativa == '0'*len(senha):
            break
        excelente = 0
        bom = 0
        for iteracao in range(len(senha)):
            if tentativa[iteracao] in senha:
                if tentativa[iteracao] == senha[iteracao]:
                    excelente += 1
                else:
                    bom += 1
        resposta = f"({excelente},{bom})"
        print(resposta)
        
        if tentativa == senha:
            break
