"""
Operadores Lógicos
and, or, not
in e not in
"""
"""
nome = "Juliana"

if 'Ju' not in nome:
    print('Executei.')
else:
    print("Existe o texto.")
"""

usuario = input('Nome de usuário: ')
senha = input('Senha do usuário: ')

usuario_bd = 'Juliana'
senha_bd = '123456'

if usuario_bd == usuario and senha_bd == senha:
    print('Você está logado no sistema')
else:
    print('Você não está logado no sistema.')