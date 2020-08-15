horaInicial: int; horaFinal: int; duracao: int;

horaInicial = int(input('Hora inicial: ')) #16
horaFinal = int(input('Hora final: ')) #2

if horaInicial == 0 and horaFinal == 0:
    duracao = 24
elif horaFinal > horaInicial:
    duracao = horaFinal - horaInicial
else:
    duracao = (horaFinal + 24) - horaInicial
print(f'O JOGO DUROU {duracao} HORA(S)')
