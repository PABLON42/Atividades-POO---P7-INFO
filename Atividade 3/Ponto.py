class Ponto(object):
    def __init__(self, x, y, P1x, P1y, P2x, P2y):
        self.__x = int(x)
        self.__y = int(y)
        self.P1x = int(P1x)
        self.P1y = int(P1y)
        self.P2x = int(P2x)
        self.P2y = int(P2y)


    def getX(self):
        return self.__x

    def getY(self):
        return self.__x

    def setX(self, x):
        self.x = x

    def setY(self, y):
        self.y = y

    def qualQuadrant(self):
        if self.__x > 0 and self.__y > 0:
            return 1

        if self.__x < 0 and self.__y > 0:
            return 2

        if self.__x < 0 and self.__y < 0:
            return 3

        if self.__x > 0 and self.__y < 0:
            return 4

        if self.__x == 0 and self.__y == 0:
            return 'Origem'