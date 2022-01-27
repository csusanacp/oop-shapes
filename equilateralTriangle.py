from shape import AbstractShape

class EquilateralTriangle(AbstractShape):
    def __init__(self, _color: str, _filled: bool, _side: float):
        AbstractShape.__init__(self, _color, _filled)
        self._side = _side
        _side = 1.0

    def geSideLength(self):
        return self._side

    def setSideLength(self, side):
        self._side = side

    def getArea(self):
        lth = self.geSideLength()
        area = (lth**2)/2
        return area

    def getPerimeter(self):
        lth = self.geSideLength()
        perimeter = (3*lth)
        return perimeter

    def __str__(self):
        return f"Equilateral Triangle[Shape " \
               f"[color: {self.getColor()}, " \
               f"filled: {self.getFilled()}, " \
               f"side length: {self.geSideLength()}cms]]"

