from Ponto_Quad import Quad


class Teste(Quad):
    def __init__(self, x, y, P1x, P1y, P2x, P2y):
        super().__init__(x, y, P1x, P1y, P2x, P2y)

    def imprimeTeste(self):
        print(f'\nPonto: {self.getX(), self.getY()}\nQuadrante {self.qualQuadrant()}')
        if self.P1x < self.P2x and self.P1y > self.P2y:
            print(f'\nP1: {self.P1}\t P2: {self.P2}')
        else:
            print('não foi possível formar o quadrilátero!')
        print(f' \n{self.contidoEmQ()}')


if __name__ == '__main__':
    x = input('digite o valor de X: ')
    y = input('digite o valor de Y: ')
    P1x = input('digite o valor de P1x: ')
    P1y = input('digite o valor de P1y: ')
    P2x = input('digite o valor de P2x: ')
    P2y = input('digite o valor de P2y: ')
    oz = Teste(x, y, P1x, P1y, P2x, P2y)
    oz.imprimeTeste()