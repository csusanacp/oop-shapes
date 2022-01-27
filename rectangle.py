from shape import Shape


class Rectangle(Shape):

    def __init__(self, _color: str, _filled, _width=float, _length=float):
        Shape.__init__(self, _color, _filled)
        self._width = _width
        self._length = _length
        _width = 1.0
        _length = 1.0

    def setWidth(self, width: float):
        self._width = width

    def getWidth(self):
        return self._width

    def setLength(self, length: float):
        self._length = length

    def getLength(self):
        return self._length

    def getArea(self):
        w = self.getWidth()
        lth = self.getLength()
        area = (lth*w)
        return area

    def getPerimeter(self):
        w = self.getWidth()
        lth = self.getLength()
        perimeter = (2*w)+(2*lth)
        return perimeter

    def __str__(self):
        return f"Rectangle[Shape[ " \
               f"[color: {self.getColor()}, " \
               f"filled: {self.getFilled()}, " \
               f"width: {self.getWidth()}cms, " \
               f"length: {self._length}cms]] "