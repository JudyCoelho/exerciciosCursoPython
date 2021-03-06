"""
* Criar variáveis para nome (str), idade (int),
* altura (float) e peso (float) de uma pessoa
* Criar variável com o ano atual (int)
* Obter o ano de nascimento da pessoa (baseado na idade e no ano atual)
* Obter o IMC da pessoa com 2 casas decimais (peso e na altura da pessoa)
* Exibir um texto com todos os valores na tela usando F-Strings (com as chaves)
"""
nome = 'Juliana'
idade = 35
altura = 1.62
peso = 68
ano_atual = 2021
ano_nascimento = 2021 - 36
imc = peso / altura ** 2

print(f'{nome} tem {idade} anos de idade, nasceu no ano de {ano_nascimento}, {altura} de altura, e seu peso é {peso}kg e seu imc é {imc:.2f}')
print(f'{nome} tem {idade} anos e {altura} de altura.')
print(f'{nome} pesa {peso}kg e seu imc é {imc:.2f}')
print(f'{nome} nasceu em {ano_nascimento}.')