from math import sin, cos, tan, radians

angulo = radians(float(input('Digite o ângulo que você deseja: ')))

print('O ângulo de {} tem o SENO de {:.3f}.'.format(angulo, sin(angulo)))
print('O ângulo de {} tem o COSSENO de {:.3f}.'.format(angulo, cos(angulo)))
print('O ângulo de {} tem o TANGENTE de {:.3f}.'.format(angulo, tan(angulo)))
