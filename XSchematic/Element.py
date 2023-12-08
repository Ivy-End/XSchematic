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
                 startPoint: Point,
                 endPoint: Point,
                 alpha : float = 1.0,
                 color : str = 'black',
                 lineWidth : float = 1.0):
        super().__init__()

        self.startPoint = startPoint
        self.endPoint = endPoint
        self.alpha = alpha
        self.color = color
        self.lineWidth = lineWidth
    
    def draw(self, canvas):
        coordinates_x = [self.startPoint.x, self.endPoint.x]
        coordinates_y = [self.startPoint.y, self.endPoint.y]
        canvas.plot(coordinates_x, coordinates_y,
                    alpha = self.alpha,
                    color = self.color,
                    linewidth = self.lineWidth)

    def __str__(self):
        return '{} -> {}'.format(self.startPoint, self.endPoint)

class PolyLine(Element):
    def __init__(self, lineSegments : list):
        super().__init__()
        
        self.lineSegments = lineSegments
    
    def draw(self, canvas):
        for line in self.lineSegments:
            line.draw(canvas)

    def __str__(self):
        return 'PolyLine: {}'.format(self.lineSegments)