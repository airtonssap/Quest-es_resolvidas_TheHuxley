#Pseudocentral, contador e listaTotal, vão ser usados para cálculos.
pseudocentral = 0
contador = 0
listaTotal = []

#ListaLoHi, que será a saída.
listaLoHi = []
#Quantidade de dinheiro exposto.
QntNotas = int(input('Dinheiro exposto: '))

#Valores dos dinheiros expostos.
listaNotas = input('Valores dos dinheiros expostos: ').split()

#Quantidade de requisições do Sr. Indeciso.
requisicoes = int(input('Requisições: '))

#Valor de cada requisição e adicionando em uma lista.
listaRequisicao = []
for requisicao in range(requisicoes):
    r = input(f'{requisicao+1}º requisição: ')
    listaRequisicao.append(r)

#Verificando, individualmente, se os valores das requisições existem na listaNotas.
for requisicao in listaRequisicao:
    maior = len(listaNotas) - 1
    menor = 0
    
    while menor <= maior:
        central = round((maior+menor)/2)
        if listaNotas[central] == requisicao:
            break
        if listaNotas[central] > requisicao:
            maior = central - 1
        else:
            menor = central + 1
            
#Se acaso existir repetição do valor da requisição, sempre o lo terá o índice igual
#ao da primeira repetição e o hi terá o índice da última repetição.
    if listaNotas[central] == requisicao:
        if listaNotas[central-1] == listaNotas[central+1]:
            pseudocentral = central
            while True:
                hi = pseudocentral + 1
                pseudocentral += 1
                if (listaNotas[pseudocentral+1] != listaNotas[pseudocentral]) or pseudocentral >= len(listaNotas)-1:
                    break
            pseudocentral = central    
            while True:
                lo = pseudocentral - 1
                pseudocentral -= 1
                if (listaNotas[pseudocentral-1] != listaNotas[pseudocentral]) or pseudocentral <= 0:
                    break
            
            listaLoHi.append([lo,hi])
            continue
                
        if listaNotas[central+1] == listaNotas[central]:
            pseudocentral = central
            contador = 0
            while True:
                pseudocentral = central
                lo = pseudocentral - contador
                hi = pseudocentral + 1
                pseudocentral += 1
                contador += 1
                if (listaNotas[pseudocentral+1] != listaNotas[pseudocentral]) or pseudocentral >= len(listaNotas)-1:
                    break
            
            listaLoHi.append([lo,hi])
            continue
        
        if listaNotas[central-1] == listaNotas[central]:
            pseudocentral = central
            contador = 0
            while True:
                lo = pseudocentral - 1
                hi = pseudocentral + contador
                pseudocentral -= 1
                contador += 1
                if (listaNotas[pseudocentral-1] != listaNotas[pseudocentral]) or pseudocentral <= 0:
                    break    
            
            listaLoHi.append([lo,hi])
            continue
        while True:
            lo = central
            hi = central
            listaLoHi.append([lo,hi])                
            break
        continue
        
#Adicionando a uma mesma lista a requisição e as Notas
#no caso de não existir valor igual de requisição na listaNotas e ordenando-a.
    if listaNotas[central] != requisicao:
        listaTotal.clear()
        listaTotal.extend(listaNotas)
        listaTotal.append(requisicao)
        listaTotal = sorted(listaTotal)
#Agora verificando a posição da requisição para pode pegar os valores dos índices lo e hi.
        maior = len(listaTotal) - 1
        menor = 0
        
        while menor <= maior:
            central = round((maior+menor)/2)
            if listaTotal[central] == requisicao:
                break
            if listaTotal[central] > requisicao:
                maior = central - 1
            else:
                menor = central + 1

#Possibilidade da requisição ser o primeiro índice.
        if central == 0:
            lo = 0
            hi = "Não existe"
            listaLoHi.append([lo,hi])
            continue

#Possibilidade da requisição ser o último índice.
        elif central == len(listaTotal) - 1:
            lo = "Não existe"
            hi = len(listaTotal) - 1
            listaLoHi.append([lo,hi])
            continue

#Possibilidade da requisição estar entre o primeiro e último índice, no caso 
#queremos o índice na listaNotas, por isso lo é central e não central + 1.
        else:
            lo = central
            hi = central - 1
            listaLoHi.append([lo,hi])

for lohi in listaLoHi:
    print(f'{lohi[0]} {lohi[1]}')