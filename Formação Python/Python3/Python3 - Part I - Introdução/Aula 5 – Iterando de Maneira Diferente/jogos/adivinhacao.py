print("*" * 37)
print("| Bem vindo ao jogo de adivinhação! |")
print("*" * 37)

numero_secreto = 42
total_de_tentativas = int(input("Quantas vezes deseja tentar?\nR: "))

for rodada in range(1, total_de_tentativas + 1):
    print('Tentativa {} de {}', format(rodada, str(total_de_tentativas)))
    chute = int(input("Digite um número entre 1 e 100!\nR: "))

    if (chute < 1 or chute > 100):
        print("\nVocê deve digitar um número entre 1 e 100!\n")
        continue

    acertou = chute == numero_secreto
    maior   = chute > numero_secreto
    menor   = chute < numero_secreto

    if (acertou):
        print('Parabéns, você acertou! O número secreto era:', numero_secreto)
        break
    else:
        if (maior):
            print('Oh não, você errou! O número secreto está mais para baixo do que seu chute')
        elif (menor):
            print('Oh não, você errou! O número secreto está mais para cima do que seu chute')

    print("\n")
    rodada += 1

print("\nFim do Jogo!")
