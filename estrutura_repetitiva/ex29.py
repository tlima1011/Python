def informarNumerosPrimos(nums):
    n = 1
    for j in range(n, nums+1):
        cont = 0
        #print(j, end=' ')
        for i in range(1, j+1):
            if j % i == 0:
                cont += 1
        if cont == 2:
            print(j, end=' ')
    return ''


nums = int(input('Quais os números: '))
print(informarNumerosPrimos(nums))