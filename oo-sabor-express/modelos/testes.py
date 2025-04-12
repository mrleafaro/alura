class Musica:
    musicas = []
    def __init__(self, nome='', artista='', duracao=0):
        self.nome = nome
        self.artista = artista
        self.duracao = duracao
        Musica.musicas.append(self)
    def __str__(self):
        return f'{self.nome} | {self.artista}'
    def listar_musicas():
        for musica in Musica.musicas:
            print(f'{musica.nome} | {musica.artista} | {musica.duracao}')
    
musica1 = Musica('Metamorphosis','INTERWORLD',2)
musica2 = Musica('Route 66', 'Chuck Berry', 2)
musica3 = Musica('Rondo Alla Turca', 'Wolfgang Amadeus Mozart', 2)

Musica.listar_musicas()

