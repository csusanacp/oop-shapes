# object-oriented programming exercise
from abc import ABC, abstractmethod
import math


class Shape(ABC):
    def __init__(self, __color=str, __filled=bool):
        self.__color = __color
        self.__filled = __filled

    def get_color(self):
        return self.__color

    def set_color(self, color):
        self.__color = color

    def get_filled(self):
        return self.__filled

    def set_filled(self,filled):
        self.__filled = filled

    @abstractmethod
    def get_area(self):
        pass

    @abstractmethod
    def get_perimeter(self):
        pass

    def __str__(self):
        return f"My new shape is:" \
               f" [color: {self.get_color()}, " \
               f"filled: {self.get_filled()}] "


class Circle(Shape):
    def __init__(self, __color, __filled, __radius=float):
        Shape.__init__(self, __color, __filled)
        self.__radius = __radius

    def get_radius(self):
        return self.__radius

    def set_radius(self, radius):
        self.__radius = radius

    def get_area(self):
        r = self.get_radius()
        area = math.pi * (r**2)
        print(f"My circle area is: {area}")
        return super().get_perimeter()

    def get_perimeter(self):
        r = self.get_radius()
        perimeter = 2*math.pi*r
        print(f"My circle perimeter is: {perimeter}")
        return super().get_perimeter()

    def __str__(self):
        return f"My new circle is:" \
               f" [color: {self.get_color()}, " \
               f"filled: {self.get_filled()}, " \
               f"radius: {self.get_radius()}cms]"


class Rectangle(Shape):

    def __init__(self, __color, __filled, __width=float, __length=float):
        Shape.__init__(self, __color, __filled)
        self.__width = __width
        self.__length = __length

    def set_width(self, width):
        self.__width = width

    def get_width(self):
        return self.__width

    def set_length(self, length):
        self.__length = length

    def get_length(self):
        return self.__length

    def get_area(self):
        w = self.get_width()
        lth = self.get_length()
        area = (lth*w)
        print(f"My rectangle area is: {area}")
        return super().get_area()

    def get_perimeter(self):
        w = self.get_width()
        lth = self.get_length()
        perimeter = (2*w)+(2*lth)
        print(f"My rectangle perimeter is: {perimeter}")
        return super().get_perimeter()

    def __str__(self):
        return f"My new rectangle is " \
               f"[color: {self.get_color()}, " \
               f"filled: {self.get_filled()}, " \
               f"width: {self.get_width()}cms, " \
               f"length: {self.__length}cms] "


class Square (Rectangle):

    def __init__(self, __color, __filled, __sq_side= float):
        Rectangle.__init__(self, __color, __filled)
        self. __sq_side = __sq_side

    def set_sq_side(self, sq_side):
        self.__sq_side = sq_side

    def get_sq_side(self):
        return self.__sq_side

    def get_area(self):
        sq = self.get_sq_side()
        area = (sq**2)
        print(f"My square area is: {area}")
        return super().get_area()

    def get_perimeter(self):
        sq = self.get_sq_side()
        perimeter = (4*sq)
        print(f"My square perimeter is: {perimeter}")
        return super().get_perimeter()

    def __str__(self):
        return f"My new square is " \
               f"[color: {self.get_color()}, " \
               f"filled: {self.get_filled()}, " \
               f"side-length: {self.get_sq_side()}cms]"


class EquilateralTriangle(Shape):
    def __init__(self, __color, __filled, __side=float):
        Shape.__init__(self, __color, __filled)
        self.__side = __side

    def get_side_length(self):
        return self.__side

    def set_side_length(self, side):
        self.__side = side

    def get_area(self):
        lth = self.get_side_length()
        area = (lth**2)/2
        print(f"My equilateral triangle area is: {area}")
        return super().get_area()

    def get_perimeter(self):
        lth = self.get_side_length()
        perimeter = (3*lth)
        print(f"My equilateral triangle perimeter is: {perimeter}")
        return super().get_perimeter()

    def __str__(self):
        return f"My new equilateral triangle is " \
               f"[color: {self.get_color()}, " \
               f"filled: {self.get_filled()}, " \
               f"side length: {self.get_side_length()}cms]"


if __name__ == "__main__":

    print('MAIN CLASS:-Shapes-')
    print('FIRST CHILD CLASS:')
    print("-Circle-")
    FirstCircle = Circle("blue", False, 23.2)
    print(FirstCircle)
    FirstCircle.get_area()
    FirstCircle.get_perimeter()
    FirstCircle.set_radius(20.0)
    FirstCircle.set_filled(True)
    print(FirstCircle)
    FirstCircle.get_area()
    FirstCircle.get_perimeter()

    print('SECOND CHILD CLASS:')
    print("-Rectangle-")
    FirstRectangle = Rectangle("black", True, 3.4, 12)
    print(FirstRectangle)
    FirstRectangle.get_area()
    FirstRectangle.get_perimeter()
    FirstRectangle.set_width(10.0)
    FirstRectangle.set_length(40.0)
    FirstRectangle.set_color("blue")
    print(FirstRectangle)
    FirstRectangle.get_area()
    FirstRectangle.get_perimeter()

    print('RECTANGLE´S FIRST SUBCLASS :')
    print("-Square-")
    FirstSquare = Square("purple", True, 5.0)
    print(FirstSquare)
    FirstSquare.get_area()
    FirstSquare.get_perimeter()
    FirstSquare.set_sq_side(2.5)
    FirstSquare.set_color("burgundy")
    print(FirstSquare)
    FirstSquare.get_area()
    FirstSquare.get_perimeter()

    print('THIRD CHILD CLASS :')
    print("-Equilateral Triangle-")
    FirstETriangle = EquilateralTriangle("white", False, 3.9)
    print(FirstETriangle)
    FirstETriangle.get_area()
    FirstETriangle.get_perimeter()
    FirstETriangle.set_side_length(2.0)
    FirstETriangle.set_color("pink")
    print(FirstETriangle)
    FirstETriangle.get_area()
    FirstETriangle.get_perimeter()












