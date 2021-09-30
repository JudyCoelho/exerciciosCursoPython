"""
Listas em Python
fatiamento
append, insert, pop, del, clear, extend, +
min, max
range
"""
"""
l1 = [1,2,3]
l2 = [4,5,6]

l2.insert(0,'banana')

print(l1)
print(l2)
"""

secreto = 'perfume'
digitadas = []

while True:
    letra = input('Digite uma letra: ')

    if len(letra) > 1:
        print('Ahhhh isso não vale, digite apenas uma letra.')
        continue

    digitadas.append(letra)

    if letra in secreto:
        print(f'UHUUULL, a letra "{letra}" existe na palavra secreta.')
    else:
        print(f'AFFFFzzz: a letra "{letra}" NÃO EXISTE na palavra secreta.')
        digitadas.pop()

    secreto_temporario = ''
    for letra_secreta in secreto:
        if letra_secreta in digitadas:
            secreto_temporario += letra_secreta
        else:
            secreto_temporario += '*'

    if secreto_temporario == secreto:
        print(f'Que legal, VOCÊ GANHOUU!!! A palavra era {secreto_temporario}.')
        break
    else:
        print(f'A palavra secreta está assim: {secreto_temporario}')

    print(secreto_temporario)

