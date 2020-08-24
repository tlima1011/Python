def calcularTempo(t, l):
    return t / l


tamanho = float(input('Informe o tamanho MB: '))
link = float(input("Informe o link de internet: "))
print(f'Tempo: {calcularTempo(tamanho, link):.0f}min')