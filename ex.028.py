from random import randint
r = randint(0, 5)
n = float(input('Digite um número entre 0 e 5: '))
print('A máquina escolheu o número {}'.format(r))
if (r == n):
    print("Você adivinhou!")
else:
    print('A máquina venceu :(')

