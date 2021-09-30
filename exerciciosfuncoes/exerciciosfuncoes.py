"""
1 - Crie uma função que exibe uma saudação com os parâmetros saudação e nome.
"""
def funcao ():
    print('Oi, como você está?')
funcao()

def saudacao (saudacao, nome):
    print(f'{saudacao} {nome}')

saudacao('Olá', 'Joãozinho')


"""
2 - Crie uma função que recebe 3 números com parâmetros e exiba a soma entre eles.
"""
def soma (n1, n2, n3):
    #if n2 > 0:
        return n1 + n2 + n3

soma = soma (8,2,1)
print(soma)


"""
3 - Crie uma função que receba 2 números . O primeiro é um valor e o segundo um percentual (ex. 10 %). 
Retorne (return) o valor do primeiro núemro somado do aumento do percentual do mesmo.
"""

def aumento_percentual(valor, percentual):
    return valor + (valor * percentual / 100)

ap = aumento_percentual(50,10)
print(ap)
ap = aumento_percentual(100,10)
print(ap)


"""
4 - Fizz Buzz - Se o parâmetro da função for divisível por 2, retorne fizz, se o parâmetro da função for divisível
por 5 e por 3, retorne FizzBuzz, caso contrário, retorne o número enviado.
"""

def fb(n):
    if n % 3 == 0 and n % 5 == 0:
        return 'fizzbuzz'
    if n % 5 == 0:
        return 'buzz'
    if n % 3 == 0:
        return 'fizz'
    return n

print(fb(15))