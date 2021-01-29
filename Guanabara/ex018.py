
from math import sin, cos, tan, radians
print('Verifique a tangente, seno e cosseno de um angulo')
an = float(input("Digite o angulo:"))
an = radians(an)
asen = sin(an)
acos = cos(an)
atan = tan(an)
print('O angulo digitado de {}° tem:\n Seno de {:.2f}\n Cosseno de {:.2f}\n Tangente de {:.2f}'.format(an, asen, acos, atan))