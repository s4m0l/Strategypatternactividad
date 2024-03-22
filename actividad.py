class Movimiento:
    def atacar(self):
        pass

    def moverse(self):
        pass

class MovimientoSoldado(Movimiento):
    def atacar(self):
        print("El soldado ataca con una espada")

    def moverse(self):
        print("El soldado se mueve a pie")

class MovimientoArquero(Movimiento):
    def atacar(self):
        print("El arquero ataca con un arco y flechas")

    def moverse(self):
        print("El arquero se mueve rápidamente")

class MovimientoCaballero(Movimiento):
    def atacar(self):
        print("El caballero ataca con una lanza")

    def moverse(self):
        print("El caballero monta a caballo")

class UnidadMilitar:
    def __init__(self, comportamiento: Movimiento):
        self.comportamiento = comportamiento

    def establecer_comportamiento(self, comportamiento: Movimiento):
        self.comportamiento = comportamiento

    def realizar_ataque(self):
        self.comportamiento.atacar()

    def realizar_movimiento(self):
        self.comportamiento.moverse()

if __name__ == "__main__":
    soldado = UnidadMilitar(MovimientoSoldado())
    arquero = UnidadMilitar(MovimientoArquero())
    caballero = UnidadMilitar(MovimientoCaballero())

    print("Soldado:")
    soldado.realizar_ataque()
    soldado.realizar_movimiento()

    print("\nArquero:")
    arquero.realizar_ataque()
    arquero.realizar_movimiento()

    print("\nCaballero:")
    caballero.realizar_ataque()
    caballero.realizar_movimiento()
