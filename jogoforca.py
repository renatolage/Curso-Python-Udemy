secreta = 'te amo muito'
digitadas = []
chances = 3

while True:
    if chances <= 0:
        print('Você Perdeu!')
        break

    letra = input('Digite uma letra: ')

    if len(letra) > 1:
        print('Isso não é uma letra')
        continue

    digitadas.append(letra)

    if letra in secreta:
        print (f'Voce acertou a letra {letra}')
    else:
        print(f'Você errou. {letra} não está na palavra secreta')
        digitadas.pop()
        chances -= 1

    secreta_temp = ''
    for letra_secreta in secreta:
         if letra_secreta in digitadas:
             secreta_temp += letra_secreta
         else:
             secreta_temp += '-'
    print(secreta_temp)





