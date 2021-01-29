from math import sqrt
print('Para calculcular a hipotenusa de um triangulo retangulo')
adj = float(input('Digite quantos centimetros tem o cateto adjacente:'))
ops = float(input('Digite quantos centimentros tem o cateto oposto:'))
hip = (adj ** 2) + (ops ** 2)
print('A hipotenusa dos catetos de {}cm e {}cm é {}cm'.format(adj, ops, sqrt(hip)))
