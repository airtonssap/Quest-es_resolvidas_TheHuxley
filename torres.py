
qnt_de_torres = int(input('Quantas torres você ganhou? '))
valores_das_torres = input('Valores das torres: ').split()
lista_das_qnt_de_vezes_da_aparicao_de_um_numero = []
lista_do_numero_que_apareceu = []



for valor in valores_das_torres:
    if valor not in lista_do_numero_que_apareceu:
        lista_das_qnt_de_vezes_da_aparicao_de_um_numero.append(valores_das_torres.count(valor))
        lista_do_numero_que_apareceu.append(valor)
        if valores_das_torres.count(valor) > 1:
            qnt_de_torres = qnt_de_torres - (valores_das_torres.count(valor) -1)
        else:
            pass
        
    else:
        pass

print(f'{max(lista_das_qnt_de_vezes_da_aparicao_de_um_numero)} {qnt_de_torres}')
