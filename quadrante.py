x: float; y: float
x = 1
y = 1

while x != 0 or y != 0:
    print('Digite os valores das coordenadas X e Y: ')
    x = float(input())
    y = float(input())
    if x > 0 and y > 0:
        print('QUADRANTE Q1')
    elif x < 0 and y > 0:
        print('QUADRANTE Q2')
    elif x < 0 and y < 0:
        print('QUADRANTE Q3')
    elif x > 0 and y < 0:
        print('QUADRANTE Q4')
    else:
        break