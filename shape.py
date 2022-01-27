# object-oriented programming exercise
from abc import ABC, abstractmethod

class AbstractShape():
    def __init__(self, _color: str, _filled: bool):
        self._color = _color
        self.__filled = _filled
        _color = "red"
        _filled = True

    def getColor(self):
        return self._color

    def setColor(self, color):
        self._color = color

    def getFilled(self):
        return self.__filled

    def setFilled(self, filled):
        self.__filled = filled

    @abstractmethod
    def getArea(self):
        pass

    @abstractmethod
    def getPerimeter(self):
        pass

    @abstractmethod
    def __str__(self):
        pass


class Shape(AbstractShape):
    def __init__(self, _color: str, _filled: bool):
        AbstractShape.__init__(self, _color, _filled)
        _color = "red"
        _filled = True













