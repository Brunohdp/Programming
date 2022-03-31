
class Cliente:
    def __init__(self, nome):
        self.__nome = nome

    @property
    def nome(self):
        print("Chamando um @property como se fosse um atributo que na verdade é um método getter")
        return self.__nome.title()

    @nome.setter
    def nome(self, nome):
        print("Chamando um @property como se fosse um atributo que na verdade é um método setter")
        self.__nome = nome
