
qnt_de_jogos = int(input('Quantos jogos serão realizados? '))

for jogos in range(qnt_de_jogos):
    tam_senha = input('Qual o tamanho da senha númerica que será utilizada? ')
    senha = input('Digite a sua senha: ')
    while True:
        valor = input('Adivinhe a senha: ')
        excelente = 0
        bom = 0
        for iteracao in range(len(senha)):
            if valor[iteracao] in senha:
                if valor[iteracao] == senha[iteracao]:
                    excelente += 1
                else:
                    bom += 1
        tupla = (excelente, bom)
        print(tupla)
        
        if valor == senha:
            break
        if valor == '0'*len(senha):
            break