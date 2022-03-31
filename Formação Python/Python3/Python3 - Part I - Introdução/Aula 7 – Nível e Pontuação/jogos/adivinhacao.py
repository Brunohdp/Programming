from random import randint

print("*" * 37)
print("* Bem vindo ao jogo de adivinhação! *")
print("*" * 37)

numero_secreto = randint(1, 100)
total_de_tentativas = 0
pontos = 1000

print("-" * 34)
print("| Escolha o nível de dificuldade |")
print("-" * 34)

nivel = int(input("| (1) Fácil   |\n| (2) Médio   |\n| (3) Difícil |\n| R: "))
print("-" * 15)

if (nivel == 1):
    total_de_tentativas = 20
elif (nivel == 2):
    total_de_tentativas = 10
else:
    total_de_tentativas = 5

for rodada in range(1, total_de_tentativas + 1):
    print("*" * 22)
    print(f'* Tentativa {rodada:02} de {total_de_tentativas:2} *')
    print("*" * 22)
    print("-" * 35)
    print("| Digite um número entre 1 e 100: |")

    print("-" * 35)
    chute = int(input("| R: ", end="|"))
    print("-" * 35)

    if (chute < 1 or chute > 100):
        print("\nVocê deve digitar um número entre 1 e 100!\n")
        continue

    acertou = chute == numero_secreto
    maior   = chute > numero_secreto
    menor   = chute < numero_secreto

    if (acertou):
        print(f'Parabéns, você acertou! O número secreto era: {numero_secreto}.\nSua pontuação foi {pontos}')
        break
    else:
        if (maior):
            print('Oh não, você errou! O número secreto está mais para baixo do que seu chute')
        elif (menor):
            print('Oh não, você errou! O número secreto está mais para cima do que seu chute')
        pontos_perdidos = abs(numero_secreto - chute)
        pontos -= pontos_perdidos

    print("\n")
    rodada += 1

print("\nFim do Jogo!")
