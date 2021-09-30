"""
Funções (def) em Python - *arg **kwargs -
Aula 16 (parte 3)
"""

def func(a1, a2, a3, a4, a5, nome=None):
    print(a1, a2, a3, a4, a5, nome)

func(1,2,3,4,5, nome='Luiz')

def func(*args):
    print(args)

lista = [1,2,3,4,5]
print(*lista, sep='-')
