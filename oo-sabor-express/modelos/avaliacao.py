class Avaliacao:
    def __init__(self, cliente, nota):
        self._cliente = cliente
        self._nota = self.validar_nota(nota)
    
    def validar_nota(self, nota):
        if 0 <= nota <= 5:
            return nota
        else:
            raise ValueError('A nota deve ser de 0 a 5')