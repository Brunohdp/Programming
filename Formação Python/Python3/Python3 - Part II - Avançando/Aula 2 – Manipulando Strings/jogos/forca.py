def jogar():
    print("*" * 37)
    print("* Bem vindo ao jogo da forca! *")
    print("*" * 37)

    palavra_secreta = "banana"

    enforcou = False
    acertou = False

    while (not enforcou and not acertou):

        chute = input("Qual letra?\nR: ").lower()
        chute = chute.strip()

        index = 0
        for letra in palavra_secreta:
            if (chute == letra):
                print(f'Encontrei a letra "{letra.upper()}" na posição "{index+1}"')
            index = index + 1

        print("jogando...")
    

    print("fim do jogo")

if (__name__ == "__main__"):
    jogar()
