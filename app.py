from restaurante import Restaurante

restuarante_praca = Restaurante("praça", "gourmet")
restuarante_praca.alternar_estado()
restuarante_praca.receber_avaliacao("thi", 5)
def main():
    Restaurante.listar_restaurantes()

if __name__ == '__main__':
    main()