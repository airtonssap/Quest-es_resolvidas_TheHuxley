lista_candidatos = []
lista = []
while True:
    CandidatoeQntmidias = input('Candidato e mídia: ').split()
    if CandidatoeQntmidias[0] == 'FIM':
        break
    lista.append(CandidatoeQntmidias[0])
    for midias in range(1,int(CandidatoeQntmidias[1])+1):
        midia = input(f'{midias}º tipo de mídia: ')
        if midia == 'radio':
            TipoRadio = input('Tipo de rádio: ')
            lista.append(TipoRadio)
        elif midia == 'tv':
            HoraTv = input('Horário da propaganda: ')
            lista.append(HoraTv)
        else:
            lista.append(midia)
    lista_candidatos.append(lista.copy())
    lista.clear()
for candidatos in lista_candidatos:
    soma = 0
    for valor in candidatos:
        if valor == 'internet':
            soma += 3000
        elif valor == 'revista':
            soma += 750
        elif valor == 'outdoor':
            soma += 1500
        elif valor == 'am':
            soma += 300
        elif valor == 'fm':
            soma += 500
        elif valor.isnumeric() == True:
            if int(valor) > 20:
                soma += 2000
            else:
                soma += 1200
    print(f'{candidatos[0]}: {soma:.2f}')