from modelos.restaurante import Restaurante
from modelos.cardapio.bebida import Bebida
from modelos.cardapio.prato import Prato

restaurante_papaspizza = Restaurante('PapasPizza', 'Pizzaria')
bebida_suco = Bebida('Suco de Laranja', 5.0,'grande')
bebida_suco.aplicar_desconto()
prato_pizza_de_mussarela = Prato('Pizza de Mussarela',40.00,'Pizza de queijo mussarela')
prato_pizza_de_mussarela.aplicar_desconto()
restaurante_papaspizza.adicionar_no_cardapio(bebida_suco)
restaurante_papaspizza.adicionar_no_cardapio(prato_pizza_de_mussarela)

def main():
    restaurante_papaspizza.exibir_cardapio

if __name__ == '__main__':
    main()