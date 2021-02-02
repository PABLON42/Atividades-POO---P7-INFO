from Ponto import Ponto


class Quad(Ponto):
    def __init__(self, x, y, P1x, P1y, P2x, P2y):
        super().__init__(x, y, P1x, P1y, P2x, P2y)
        self.P1 = self.P1x, self.P1y
        self.P2 = self.P2x, self.P2y

    def contidoEmQ(self):
        if self.P1[0] < self.getX() < self.P2[0] and self.P1[1] > self.getY() > self.P2[1]:
            return True

        else:
            return False