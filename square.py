from rectangle import Rectangle


class Square (Rectangle):

    def __init__(self, _color: str, _filled: bool, _side: float):
        Rectangle.__init__(self, _color, _filled, _side, _side)

    def getSide(self):
        self.getLength()

    def setSide(self, side: float):
        self.setLength(side)
        self.setWidth(side)

    def setLenght(self, lenght: float):
        self.setSide(lenght)

    def setWidth(self, width: float):
        self.setSide(width)

    def __str__(self):
        return f"Square[Rectangle " \
               f"[color: {self.getColor()}, " \
               f"filled: {self.getFilled()}, " \
               f"side-length: {self.getSide()}cms]]"

