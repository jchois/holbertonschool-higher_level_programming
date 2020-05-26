#!/usr/bin/python3
'''
This module has in it the class `Rectangle`.
'''


class Rectangle:
    '''
    Thiss class defines a rectangle.
    '''

    number_of_instances = 0
    print_symbol = '#'

    def __init__(self, width=0, height=0):
        '''
        This is the initialize constructor for `rectangle`
        ARGUMENTS:
        → width {int} is the width of the `rectangle`. [deafult: 0]
        → height {int} is the height of the `rectangle`. [deafult: 0]
        '''
        self.width = width
        self.height = height

        Rectangle.number_of_instances += 1

    @property
    def width(self):
        '''
        This is the width getter of `rectangle`.
        '''
        return (self.__width)

    @width.setter
    def width(self, value):
        '''
        This is the width setter of `rectangle`.
        ARGUMENTS:
        → value {int} is the width value for the `rectangle`
        '''
        if not isinstance(value, int):
            raise TypeError('width must be an integer')
        if value < 0:
            raise ValueError('width must be >= 0')
        self.__width = value

    @property
    def height(self):
        '''
        This is the height getter of `rectangle`.
        '''
        return (self.__height)

    @height.setter
    def height(self, value):
        '''
        This is the height setter of `rectangle`.
        ARGUMENTS:
        → value {int} is the height value for the `rectangle`
        '''
        if not isinstance(value, int):
            raise TypeError('height must be an integer')
        if value < 0:
            raise ValueError('height must be >= 0')
        self.__height = value

    def area(self):
        '''
        This is the `rectangle`'s area operation.
        '''
        return (self.__width * self.__height)

    def perimeter(self):
        '''
        This is the `rectangle`'s perimeter operation.
        '''
        if self.__height == 0 or self.__width == 0:
            return (0)
        return (2 * (self.__width + self.__height))

    def __str__(self):
        '''
        This function returns a `rectangle`'s graphic.
        '''
        if self.height == 0 or self.width == 0:
            return ("")
        w = "#" * self.width
        printed = w
        for _i in range(self.height-1):
            printed += "\n" + w
        return (printed)

    def __repr__(self):
        '''
        This function returns a `rectangle`'s graphic.
        '''
        return "Rectangle({}, {})".format(self.__width, self.__height)

    def __del__(self):
        '''
        This function returns message on deleting `rectangle`.
        '''
        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        '''
        This function returns the `Rectangle` instance with bigger area.
        ARGUMENTS:
        → rect_1 {Rectangle} is an instance of `Rectangle`.
        → rect_2 {Rectangle} is an instance of `Rectangle`.
        '''
        if not isinstance(rect_1, Rectangle):
            raise TypeError('rect_1 must be an instance of Rectangle')
        if not isinstance(rect_2, Rectangle):
            raise TypeError('rect_2 must be an instance of Rectangle')
        r1, r2 = rect_1.area(), rect_2.area()
        if r2 > r1:
            return (rect_2)
        return (rect_1)

    @classmethod
    def square(cls, size=0):
        '''
        It transforms a rectangle into square.
        ARGUMENTS:
        → size {int} is the new size for the Rectangle.
        '''
        return cls(size, size)
