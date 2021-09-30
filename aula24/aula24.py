"""
Funções - def em Python (Parte 1)
"""

def funcao():
    print("Hello World!")
funcao()
funcao()
funcao()
funcao()

"""
Funções (def) em Python - return - Aula 16 (Parte 2)
"""

def divisao(n1, n2):
    if n2 > 0:
        return n1 / n2

divide = divisao(8,2)

if divide:
    print(divide)
else:
    print('Conta inválida.')

