from modelos.restaurante import Restaurante

restuarante_praca = Restaurante("praça", "gourmet")
restuarante_praca.receber_avaliacao("thi", 10)
def main():
    Restaurante.listar_restaurantes()

if __name__ == '__main__':
    main()