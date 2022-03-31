# class Filme:
    def __init__(self, nome, ano, duracao):
        self.__nome = nome.title()
        self.ano = ano
        self.duracao = duracao
        self.__likes = 0

    @property
    def likes(self):
        return self.__likes

    @property
    def nome(self):
        return self.__nome

    def dar_like(self):
        self.__likes += 1

    @nome.setter
    def nome(self, novo_nome):
        self.__nome = novo_nome.title()

class Series:
    def __init__(self, nome, ano, temporadas):
        self.__nome = nome.title()
        self.ano = ano
        self.temporadas = temporadas
        self.__likes = 0

    @property
    def likes(self):
        return self.__likes

    @property
    def nome(self):
        return self.__nome

    def dar_like(self):
        self.__likes += 1

    @nome.setter
    def nome(self, novo_nome):
        self.__nome = novo_nome.title()


vingadores = Filme('Vingadores - guerra infinita', 2018, 160)
print(f'Nome: {vingadores.nome}. Ano: {vingadores.ano}. '
      f'Duração: {vingadores.duracao}. Likes: {vingadores.likes}')


atlanta = Series('Atlanta', 2018, 2)
atlanta.dar_like()
atlanta.dar_like()
print(f'Nome: {atlanta.nome}. Ano: {atlanta.ano}. '
      f'Temporadas: {atlanta.temporadas}. Likes: {atlanta.likes}')
