import random

def jogar():
    print("*" * 37)
    print("* Bem vindo ao jogo da forca! *")
    print("*" * 37)

    arquivo = open("palavras.txt", "r")
    palavras = []

    for linha in arquivo:
        linha = linha.strip()
        palavras.append(linha)

    arquivo.close()

    numero = random.randrange(0, len(palavras))
    palavra_secreta = palavras[numero].upper()

    letras_acertadas = ["_" for letra in palavra_secreta]

    enforcou = False
    acertou = False
    erros = 0

    print(letras_acertadas)

    while (not enforcou and not acertou):

        chute = input("Qual letra?\nR: ").upper()
        chute = chute.strip()

        if (chute in palavra_secreta):
            index = 0
            for letra in palavra_secreta:
                if (chute == letra):
                    letras_acertadas[index] = letra
                index += 1
        else:
            erros += 1

        enforcou = erros == 6
        acertou = "_" not in letras_acertadas
        print(letras_acertadas)


    if (acertou):
        print(f'Você ganhou:D. A palavra secreta era {palavra_secreta}. Parabéns!!')
    else:
        print(f'Ah não, você perdeu :(. A palavra secreta era {palavra_secreta}. Quem sabe na próxima ;)')
    print("fim do jogo")


if (__name__ == "__main__"):
    jogar()
