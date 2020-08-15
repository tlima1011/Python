duracao: int; segundos: int; minutos: int; horas: int; resto: int

duracao = int(input('Digite a duracao em segundos: '))

horas = duracao // 3600
resto = duracao % 3600
minutos = resto // 60
segundos = resto % 60
print (f"{horas}hh: {minutos} mm {segundos} s.")

#0:5:0