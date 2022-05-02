
limite = int(input('Digite um valor n, tal que 1 <= n <= 40: '))
inicio = 1
palavra = str(inicio)
while inicio < limite:
    print(palavra)
    inicio += 1
    palavra += ' ' + str(inicio)

print(palavra)
