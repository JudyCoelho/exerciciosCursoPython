
"""
Faça um programa que peça ao usuário para digitar um número inteiro,
informe se este número é par ou impar. Caso o usuário não digite um número inteiro,
informe que não é um número interio.
"""
""" exemplo1
numero = input("Digite um número inteiro: ")

if not numero.isdigit():
    print('Isso não é um número inteiro.')
else:
    numero = int(numero)
    if not numero % 2 == 0:
        print(f"{numero} é ímpar")
    else:
        print(f"{numero} é par.")
"""



""" 
Faça um programa que pergunte a hora ao uusário e, baseando-se no horário descrito, exiba a saudação apropriada.
Ex. Bom dia 0-11, boa tarde 12-17 e Boa noite 18-23.
"""
""" exemplo 2
horario = input('Digite um horário (0-23): ')

if horario.isdigit():
    horario = int (horario)

    if horario < 0 or horario > 23:
        print("Horário deve estar entre 0 e 23.")
    else:
        if horario < 11:
            print('Bom dia!')
        elif horario <= 17:
            print('Boa tarde!')
        else:
            print('Boa noite!')
else:
    print("Por favor, digite um horário entre 0 e 23.")
"""



"""
Faça um programa que peça o primeiro nome do usuário. Se o nome tiver 4 letras ou
menos escreva "Seu nome é curto"; se tiver entre 5 e 6 letras, escreva "Seu nome é normal, maior que 6 escreve
"seu nome é muito grande."
"""

nome = input('Digite seu nome: ')
tamanho = len(nome)

if tamanho <= 4:
    print('Seu nome é curto.')
elif tamanho <= 6:
    print('Seu nome é normal.')
else:
    print('Seu nome é muito grande.')


