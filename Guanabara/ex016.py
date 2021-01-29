from math import trunc as t
print('Digite a seguir um número real para verificar sua porção inteira')
num = float(input('Digite o número desejado:'))
print('A porção inteira de {} é {}.'.format(num, t(num)))
