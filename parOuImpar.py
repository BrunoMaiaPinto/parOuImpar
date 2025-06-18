import random

vidas = 3
pontos = 0

while (vidas):
  number = random.randint(0, 201)
  aposta = input('Par ou Ímpar? ').lower()
  if (aposta == "par" and number % 2 == 0 or aposta == "impar" and number % 2 != 0):
    pontos += 10
    print(f'{number} - Acertou!')
  else:
    vidas -= 1
    print(f'{number} - Errou!')

  
print(f'\nGame Over!\nPontos: {pontos}')