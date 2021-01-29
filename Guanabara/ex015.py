# calculo de aluguel de carro
print('Calculo de aluguel de veículo ')
dias = int(input('Por quantos dias o carro foi alugado? :'))
km = float(input('Quantos Km foram rodados no veículo? :'))
va = 60 * dias + km * 0.15
print('O valor do aluguel a ser pago é R${}.'.format(va))
print('Detalhe do valor a ser cobrado:')
print('Dias\n {}'.format(dias), '-'*12, 'valor R${}'.format(dias * 60))
print('Kilometros rodados\n {}'.format(km), '-'*10, 'Valor R${}'.format(km * 0.15))
