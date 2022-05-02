
def leet(palavra = '0'):
    alteracao = 0
    if len(palavra) == 0:
        palavra = 'oizav'
        alteracao = 0
    else:
        for caractere in palavra:
            if caractere.isnumeric() == True:
                palavra = 'soremun'
                alteracao = '0'
                break
            elif caractere == 'a' or caractere == 'A':
                palavra = palavra.replace(caractere, '@')
                alteracao += 1
            elif caractere == 'e' or caractere == 'E':
                palavra = palavra.replace(caractere, '3')
                alteracao += 1
            elif caractere == 'i' or caractere == 'I':
                palavra = palavra.replace(caractere, '1')
                alteracao += 1
            elif caractere == 'o' or caractere == 'O':
                palavra = palavra.replace(caractere, '0')
                alteracao += 1
            elif caractere == 't' or caractere == 'T':
                palavra = palavra.replace(caractere, '7')
                alteracao += 1
            elif caractere == 's' or caractere == 'S':
                palavra = palavra.replace(caractere, '5')
                alteracao += 1
    return [palavra[::-1], alteracao]

palavra = input('Digite seu texto/palavra aqui: ')
print(leet(palavra)[0])
print(leet(palavra)[1])

