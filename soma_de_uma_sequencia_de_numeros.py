qnt_de_elementos = int(input('Quantidade de elementos que deseja somar: '))
lista = []
for iteracao in range(qnt_de_elementos):
    valor = int(input(f'Digite o valor do {iteracao+1}º elemento: '))
    lista.append(valor)
print(sum(lista))