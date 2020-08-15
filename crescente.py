x: int; y: int;

print('Digite dois numeros:')
while True:
    x = int(input())
    y = int(input())
    if x > y:
        print('DECRESCENTE!')
    elif y > x:
        print('CRESCENTE!')
    else:
        break
    print('Digite outros dois numeros:')

