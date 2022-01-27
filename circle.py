from shape import Shape
import math


class Circle(Shape):
    def __init__(self, _color, _filled, _radius=float):
        Shape.__init__(self, _color, _filled)
        self._radius = _radius
        _radius = 1.0

    def getRadius(self):
        return self._radius

    def setRadius(self, radius):
        self._radius = radius

    def getArea(self):
        r = self.getRadius()
        area = math.pi * (r**2)
        return area

    def getPerimeter(self):
        r = self.getRadius()
        perimeter = 2*math.pi*r
        return perimeter

    def __str__(self):
        return f"Circle[Shape" \
               f"[color: {self.getColor()}, " \
               f"filled: {self.getFilled()}, " \
               f"radius: {self.getRadius()}cms]]"

