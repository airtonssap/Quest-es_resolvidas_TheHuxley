while True:
    idade = int(input('Qual sua idade: '))
    if idade > 65:
        print('Você é um idoso.')
    elif idade > 35:
        print('Você é um adulto.')
    elif idade > 17:
        print('Você é um jovem.')
    elif idade > 11:
        print('Você é um adolescente.')
    elif idade > 0:
        print('Você é uma criança.')
    elif idade < 0:
        print('a pessoa ainda não nasceu')
    else:
        break
