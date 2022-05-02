
def contarDigitos(numero):
    if len(str(numero)) !=4:
        return False

    else:
        return True

def ehBissexto(valor):
    if contarDigitos(valor) == True:
        if valor%4 == 0 and (valor%100 != 0 or valor%400 == 0):
            return True
        else:
            return False

    else:
        return False

def Mensagem(valor):
    if (ehBissexto(valor) == True) and (contarDigitos(valor) == True):
        if valor == 2152:
            return 'O ano 2152 eh bissexto'
        elif valor < 2152:
            return f'O ano {valor} foi bissexto'
        else:
            return f'O ano {valor} serah bissexto'

    elif (ehBissexto(valor) == False) and (contarDigitos(valor) == True):
        return f'O ano {valor} NAO eh bissexto'

    else:
        return 'Ano invalido'

while True:
    n = int(input('Insira um ano de 4 dígitos: '))
    if n == -1:
        break
    contarDigitos(n)
    ehBissexto(n)
    print(Mensagem(n))
