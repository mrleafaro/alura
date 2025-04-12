from avaliacao import Avaliacao
from modelos.cardapio.item_cardapio import ItemCardapio
from cardapio.prato import Prato
from cardapio.bebida import Bebida

class Restaurante:
    restaurantes = []

    def __init__(self, nome, categoria):
        self._nome = nome.title()  # Capitaliza o nome
        self._categoria = categoria.upper()  # Coloca a categoria em letras maiúsculas
        self._ativo = False  # Estado inicial do restaurante
        self._avaliacao = []  # Lista de avaliações
        self._cardapio = [] # Lista do cardápio
        Restaurante.restaurantes.append(self)  # Adiciona o restaurante à lista de restaurantes

    def __str__(self):
        return f'{self._nome} | {self._categoria}'

    @classmethod
    def listar_restaurantes(cls):
        # Corrigido para escapar chaves dentro de f-string
        print(f"{'Nome do restaurante'.ljust(25)} | {'Categoria'.ljust(25)} | {'Avaliação'.ljust(25)} |{'Status'}")
        for restaurante in cls.restaurantes:
            print(f'{restaurante._nome.ljust(25)} | {restaurante._categoria.ljust(25)} | {str(restaurante.media_avaliacoes).ljust(25)} | {restaurante.ativo}')

    @property
    def ativo(self):
        # Retorna ícone de ativo ou inativo
        return '✅' if self._ativo else '❌'

    def alternar_estado(self):
        # Alterna entre ativo e inativo
        self._ativo = not self._ativo

    def receber_avaliacao(self, cliente, nota):
        # Cria e adiciona uma avaliação à lista de avaliações
        avaliacao = Avaliacao(cliente, nota)
        self._avaliacao.append(avaliacao)

    @property
    def media_avaliacoes(self):
        # Calcula a média das avaliações
        if not self._avaliacao:
            return '-'
        soma_das_notas = sum(avaliacao._nota for avaliacao in self._avaliacao)
        quantidade_de_notas = len(self._avaliacao)
        media = round(soma_das_notas / quantidade_de_notas, 1)
        return media
    
    def adicionar_no_cardapio(self,item):
        if isinstance(item, ItemCardapio):
            self._cardapio.append(item)
    @property
    def exibir_cardapio(self):
        print(f'Cardápio do restaurante {self._nome}\n')
        for i, item in enumerate(self._cardapio, start=1):
            if hasattr(item, 'descricao'):  # Assume que é um Prato
                mensagem = f'{i}. Nome: {item._nome} | Preço: R${item._preco:.2f} | Descrição: {item.descricao}'
            elif hasattr(item, 'tamanho'):  # Assume que é uma Bebida
                mensagem = f'{i}. Nome: {item._nome} | Preço: R${item._preco:.2f} | Tamanho: {item.tamanho}'
        else:
            mensagem = f'{i}. Tipo desconhecido: {type(item)}'
        print(mensagem)


