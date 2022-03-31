print("*"*37)
print("| Bem vindo ao jogo de adivinhação! |")
print("*"*37)

numero_secreto = 42

chute = int(input("Digite um número!\nR: "))

if (chute == numero_secreto):
    print('Parabéns, você acertou! O número secreto era:', numero_secreto)
else:
    print('Oh não, você errou! O número secreto era:', numero_secreto)

print("\nFim do Jogo!")
