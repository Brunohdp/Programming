def jogar():
    print("*" * 37)
    print("* Bem vindo ao jogo da forca! *")
    print("*" * 37)

    palavra_secreta = "banana"
    letras_acertadas = ["_", "_", "_", "_", "_", "_"]

    enforcou = False
    acertou = False

    print(letras_acertadas)

    while (not enforcou and not acertou):

        chute = input("Qual letra?\nR: ").lower()
        chute = chute.strip()

        index = 0
        for letra in palavra_secreta:
            if (chute == letra):
                letras_acertadas[index] = letra
            index = index + 1

        print(letras_acertadas)

    print("fim do jogo")


if (__name__ == "__main__"):
    jogar()
