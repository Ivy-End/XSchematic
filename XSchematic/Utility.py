from typing import Self

class Point:
    ''' Point class for storing x and y coordinates of a point '''

    def __init__(self, x : float, y : float) -> None:
        ''' Initialize a point with x and y coordinates '''
        super().__init__()
        self.x = x
        self.y = y
    
    def __add__(self, other: Self) -> Self:
        ''' Overload operator + '''
        try:
            return Point(self.x + other.x, self.y + other.y)
        except:
            raise TypeError('Unsupported operand type(s) for +: \'Point\' and \'{}\''.format(type(other)))

    def __sub__(self, other: Self) -> Self:
        ''' Overload operator - '''
        try:
            return Point(self.x - other.x, self.y - other.y)
        except:
            raise TypeError('Unsupported operand type(s) for -: \'Point\' and \'{}\''.format(type(other)))
    
    def __mul__(self, other: float) -> Self:
        ''' Overload operator * '''
        try:
            return Point(self[0] * other, self[1] * other)
        except:
            raise TypeError('Unsupported operand type(s) for *: \'Point\' and \'{}\''.format(type(other)))
    
    def __truediv__(self, other: float) -> Self:
        ''' Overload operator / '''
        try:
            return Point(self[0] / other, self[1] / other)
        except:
            raise TypeError('Unsupported operand type(s) for /: \'Point\' and \'{}\''.format(type(other)))

    def __neg__(self) -> Self:
        ''' Overload operator - '''
        return Point(-self.x, -self.y)
    
    def __eq__(self, other: Self) -> bool:
        ''' Overload operator == '''
        try:
            return self.x == other.x and self.y == other.y
        except:
            raise TypeError('Unsupported operand type(s) for ==: \'Point\' and \'{}\''.format(type(other)))
    
    def __ne__(self, other: Self) -> bool:
        ''' Overload operator != '''
        try:
            return self.x != other.x or self.y != other.y
        except:
            raise TypeError('Unsupported operand type(s) for !=: \'Point\' and \'{}\''.format(type(other)))
    
    def __str__(self) -> str:
        ''' Overload operator str() '''
        return '({}, {})'.format(self.x, self.y)
