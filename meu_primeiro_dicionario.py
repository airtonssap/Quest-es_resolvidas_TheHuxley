
biblioteca = dict()
lista = []
proibidos = ['.','"', '(', '*', '$', '#', ':']

while True:
    texto = input('Digite seu texto: ').lower()
    if texto == '-1':
        break
    #for valor in range(len(texto)):
    #    if texto[valor] in proibidos:
    #        texto = texto.replace(texto[valor],' ')
    for valor in texto:
        if valor in proibidos:
            texto = texto.replace(valor, ' ')
    texto = texto.split()
    lista.extend(texto.copy())

lista = sorted(lista)

for valor in lista:
    biblioteca[valor] = lista.count(valor)

for chave, valor in biblioteca.items():
    print(f'{chave} {valor}')
