# object oriented programming exercise

class Shape:
    def __init__(self, __color, __filled):
        self.__color = __color
        self.__filled = __filled

    def get_color(self):
        return self.__color

    def set_color(self,color):
        self.__color = color

    def get_filled(self):
        return self.__filled

    def set_filled(self,filled):
        self.__filled = filled


class Circle(Shape):
    def __init__(self, __color, __filled, __radius):
        Shape.__init__(self, __color, __filled)
        self.__radius= __radius

    def get_radius(self):
        return self.__radius

    def set_radius(self, radius):
        self.__radius = radius


class Rectangle(Shape):

    def __init__(self, __color, __filled, __width, __length):
        Shape.__init__(self, __color, __filled)
        self.__width = __width
        self.__length = __length

    def get_width(self):
        return self.__width

    def set_width(self, width):
        self.__width = width

    def get_length(self):
        return self.__length

    def set_length(self,length):
        self.__length = length


class Square (Rectangle):

    def __init__(self, __color, __filled, __width, __length):
        Rectangle.__init__(self, __color, __filled, __width, __length)


class EquilateralTriangle(Shape):
    def __init__(self, __color, __filled, __side):
        Shape.__init__(self, __color, __filled)
        self.__side = __side

    def get_sidelength(self):
        return self.__sidelength

    def set_sidelength(self, side):
        self.__side = side









