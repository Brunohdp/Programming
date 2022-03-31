print("*"*37)
print("| Bem vindo ao jogo de adivinhação! |")
print("*"*37)

#Números para o jogo
numero_secreto = 42
chute = int(input("Digite um número!\nR: "))

#Condições
acertou = chute == numero_secreto
maior   = chute > numero_secreto
menor   = chute < numero_secreto

if (acertou):
    print('Parabéns, você acertou! O número secreto era:', numero_secreto)
else:
    if (maior):
        print('Oh não, você errou! O número secreto está mais para baixo do que seu chute')
    elif (menor):
        print('Oh não, você errou! O número secreto está mais para cima do que seu chute')

print("\nFim do Jogo!")
