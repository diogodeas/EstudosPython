import re
import sys
import random

cpf = ''
for i in range(9):
    cpf += str(random.randint(0,9))

#entrada = input('CPF[746.824.890-70]: ')
#cpf = re.sub(r'[^0-9]', '', entrada)

entradarep = cpf == cpf[0]*len(cpf)
if entradarep:
    print('CPF invalido')
    sys.exit()
     
digitos1 = cpf
contadorRegressivo1 = 10
resultado1 = 0;

for numero1 in digitos1:
    resultado1 += (int(numero1) * contadorRegressivo1)
    contadorRegressivo1 -= 1

numero1 = (resultado1 * 10) % 11

numero1 = numero1 if numero1 <= 9 else 0

digitos2 = f'{cpf}{numero1}'
contadorRegressivo2 = 11
resultado2 = 0

for numero2 in digitos2:
    resultado2 += (int(numero2) * contadorRegressivo2)
    contadorRegressivo2 -= 1

numero2 = (resultado2 * 10) % 11

numero2 = numero2 if numero2 <= 9 else 0

cpfGerado = f'{digitos1}{numero1}{numero2}'

print(cpfGerado)
'''if cpfGerado == cpf:
    print(f'{cpf} é válido.')
else:
    print('CPF inválido')'''