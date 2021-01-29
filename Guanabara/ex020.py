#o principio do exercicio é exibir uma lista randomica de nomes, tendo como base a o exercico 19, posso usar o comando choices com valor de referencia para ser exibido como 4
from random import choices
print('Para selicionar a ordem de apresentação dos trabalhos:')
a1 = str(input('Digite o nome do primeiro aluno:'))
a2 = str(input('Digite o nome do proxímo aluno:'))
a3 = str(input('Digite o nome do proxímo aluno:'))
a4 = str(input('Digite o nome do proxímo aluno:'))
lista = a4, a3, a2, a1
print('A ordem de apresentação é:\n {}'.format(choices(lista, k=4)))
