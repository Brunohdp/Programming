import forca
import adivinhacao

print("*" * 32)
print("* Bem vindo ao Lobby de games! *")
print("*" * 32)

print("-" * 23)
print("| Escolha o seu jogo: |")
print("-" * 23)
print("| (1) Adivinhação     |\n| (2) Forca           |")
jogo = int(input("| R:"))
print("-" * 23)

if (jogo == 1):
    print('-' * 24)
    print("| Jogando Adivinhação! |")
    print('-' * 24)
    adivinhacao.jogar()
else:
    print("-" * 18)
    print("| Jogando Forca! |")
    print("-" * 18)
    forca.jogar()
