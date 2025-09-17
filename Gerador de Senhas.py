import random
senha = ''
letras = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
numeros = '0123456789'
simbulos = '!@#$%¨&*_+;:,.?-'
for j in range(3):
    senha += random.choice(numeros)
    senha += random.choice(letras)
    senha += random.choice(simbulos)
print(f'Senha gerada com sucesso!\n{senha}')