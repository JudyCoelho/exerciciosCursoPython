"""
Operadores Relacionais
== Igualdade
> maior que
>= maior ou igual a
< menor que
<= menor que
!= diferente
"""

num_1 = 2
num_2 = 2

expressao = num_1 == num_2
print(expressao)

nome = input('Qual o seu nme? ')
idade = input(' Qual a sua idade? ')

idade = int(idade)

#Limite para pegar empréstimo
idade_menor = 20 #muito jovem
idade_maior = 30 # passou da idade

if idade >= idade_menor and idade <= idade_maior:
    print(f'{nome} pode pegar o empréstimo.')
else:
    print(f'{nome} Não pode pegar o empréstimo.')

