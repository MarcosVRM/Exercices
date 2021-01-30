class Programa:
    def __init__(self, nome, ano):
        self._nome = nome.title()
        self.ano = ano
        self._likes = 0

    @property
    def like(self):
        return self._likes

    def dar_likes(self):
        self._likes += 1

    @property
    def nome(self):
        return self._nome

    @nome.setter
    def nome(self, novo_nome):
        self._nome = novo_nome.title()

    def __str__(self):
        return f'{self._nome} - Ano: {self.ano}\n Likes: {self._likes}'

class Filme(Programa):
    def __init__(self, nome, ano, duracao):
        super().__init__(nome, ano)
        self.duracao = duracao

    def __str__(self):
        return f'{self._nome} - Ano: {self.ano} - {self.duracao} min\n Likes: {self._likes}'

class Serie(Programa):
    def __init__(self, nome, ano, temporadas):
        super().__init__(nome, ano)
        self.temporadas = temporadas

    def __str__(self):
        return f'{self._nome} - Ano: {self.ano} - {self.temporadas} Temporadas\n Likes: {self._likes}'

class Playlist:
    def __init__(self, nome, programa):
        self._nome = nome
        self._programa = programa

    def __getitem__(self, item):
        return self._programa[item]

    def __len__(self):
        return len(self._programa)


vingadores = Filme("Vingadores - Guerra Infinita", 2018, 160)
friends = Serie("F.R.I.E.N.D.S", 1994, 9)
theboys = Serie("The Boys", 2019, 2)
warcraft = Filme("Warcraft - O Primeiro encontro de dois mundos", 2016, 123)
atlanta = Serie("atlanta", 2018, 2)
atlanta.dar_likes()
vingadores.dar_likes()
vingadores.dar_likes()
warcraft.dar_likes()
warcraft.dar_likes()
warcraft.dar_likes()
warcraft.dar_likes()
warcraft.dar_likes()
warcraft.dar_likes()
friends.dar_likes()
friends.dar_likes()
friends.dar_likes()
friends.dar_likes()
friends.dar_likes()
vingadores.dar_likes()
theboys.dar_likes()
theboys.dar_likes()
theboys.dar_likes()
theboys.dar_likes()
theboys.dar_likes()


lista = [vingadores, friends, atlanta, warcraft, theboys]
playlist = Playlist("minha_playlist", lista)

print(f"A Playlist contem {len(playlist)} programas\n")

for programa in playlist:
    print(programa)
