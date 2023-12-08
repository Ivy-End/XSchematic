from abc import abstractmethod
from .Utility import Point

class Element:
    def __init__(self):
        pass
    
    @abstractmethod
    def draw(self, canvas):
        raise NotImplemented

class Line(Element):
    def __init__(self,
                 start: Point,
                 end: Point):
        super().__init__()

        self.start = start
        self.end = end
    
    def draw(self, canvas):
        coordinates_x = [self.start.x, self.end.x]
        coordinates_y = [self.start.y, self.end.y]
        canvas.plot(coordinates_x, coordinates_y)

    def __str__(self):
        return '{} -> {}'.format(self.start, self.end)