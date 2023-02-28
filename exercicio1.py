"""
Faça um programa que peça ao usuário para digitar um número inteiro,
informe se este número é par ou ímpar. Caso o usuário não digite um número
inteiro, informe que não é um número inteiro.

numerostr = input('Digite um número inteiro: ')

try: 
    numero_int = int(numerostr)
    if (numero_int % 2) == 0:
        print('O número é par')
    else:
        print('O número é ímpar')
except:
    print('Isso não é um inteiro') 

Faça um programa que pergunte a hora ao usuário e, baseando-se no horário 
descrito, exiba a saudação apropriada. Ex. 
Bom dia 0-11, Boa tarde 12-17 e Boa noite 18-23.

numerostr = input('Digite a hora: ')

try: 
    numero_int = float(numerostr)

except:
    print('Isso não é um horário') 

if numero_int >= 0 and numero_int < 12:
    print('Bom dia')
elif numero_int > 12 and numero_int < 18:
    print('Boa tarde')
elif numero_int > 18 and numero_int <= 24:
    print('Boa noite')
else:
    print('Isso não é um horário') 

Faça um programa que peça o primeiro nome do usuário. Se o nome tiver 4 letras ou 
menos escreva "Seu nome é curto"; se tiver entre 5 e 6 letras, escreva 
"Seu nome é normal"; maior que 6 escreva "Seu nome é muito grande". 
"""
nome = input('Digite seu nome ')
tamanho = len(nome)
if tamanho <= 4:
    print("Seu nome é curto") 
elif tamanho > 4 and tamanho <= 6:
    print("Seu nome é normal") 
else:
    print("Seu nome é muito grande") 