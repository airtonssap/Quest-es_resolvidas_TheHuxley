
from itertools import count


texto = input('Digite seu texto: ')
texto = sorted(texto, reverse= True)
biblioteca = dict()
for letra in texto:
    biblioteca[letra] = texto.count(letra)
for chave, valor in biblioteca.items():
    print(f'{chave} {valor}')
