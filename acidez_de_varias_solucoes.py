valor = float(input('Digite o ph da solução: '))
while valor != -1:
    if valor < 7:
        print('ACIDA')

    elif valor == 7:
        print('NEUTRA')

    else:
        print('BASICA')
    
    valor = float(input('Digite o ph da solução: '))
    
