import random
tamanho = 10
senha = ''
letras = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
numeros = '0123456789'
simbolos = '!@#$%¨&*_+;:,.?-'
for j in range(tamanho):
    senha += random.choice(numeros + letras + simbolos)
print(f'Senha gerada com sucesso!\n{senha}')