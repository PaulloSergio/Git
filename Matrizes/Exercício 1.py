
''' Leia uma matrzi 4 x 4, imprima a matrzi e retorne a localização (linha e coluna) do maior valor. '''

m = []
z = 0
maior_valor = []

for i in range(1, 5):
    linha = []
    for n in range(1, 5):
        if  i == n:
            linha.append(n** 3)
        else:
            linha.append(i * n)
    m.append(linha)
    
for im, vm in enumerate(m):
    if z <= max(vm):
        z = max(vm)
        maior_valor.clear()
        maior_valor.append([im + 1, vm.index(z) + 1])

for i in maior_valor:
    print(f'Maior valor está na linha {i[0]} coluna {i[1]}')

for x in m:
    print(x)
