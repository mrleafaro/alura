from restaurante import Restaurante
from cardapio.bebida import Bebida
from cardapio.prato import Prato

restaurante_sushininja = Restaurante('Sushi Ninja', 'JAPONESA')
restaurante_blackdog = Restaurante('Black Dog', 'CACHORRO-QUENTE')
bebida_suco = Bebida('Suco de Melancia', 8.00, 'Médio')
prato_salgado = Prato('Crostini', 15.00, 'Crosta salgada e crocante, temperada com azeite e orégano')

restaurante_sushininja.receber_avaliacao('Chad', 5)
restaurante_sushininja.receber_avaliacao('Chad', 2)

restaurante_blackdog.receber_avaliacao('Giga', 3)
restaurante_blackdog.receber_avaliacao('Giga', 5)

restaurante_sushininja.adicionar_no_cardapio(bebida_suco)
restaurante_sushininja.adicionar_no_cardapio(prato_salgado)



restaurante_sushininja.alternar_estado()
def main():
    restaurante_sushininja.exibir_cardapio
if __name__ == '__main__':
    main()