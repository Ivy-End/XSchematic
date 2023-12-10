from abc import abstractmethod
from typing import Self
from .Utility import Point

class Drawable:
    def __init__(self) -> None:
        pass
    
    @abstractmethod
    def draw(self, canvas) -> None:
        raise NotImplemented

    @abstractmethod
    def __str__(self) -> str:
        raise NotImplemented

class Line(Drawable):
    def __init__(self,
                 startPoint: Point,
                 endPoint: Point,
                 color : str = 'black',
                 lineWidth : float = 1.0) -> None:
        super().__init__()

        self.startPoint = startPoint
        self.endPoint = endPoint
        self.color = color
        self.lineWidth = lineWidth
    
    def draw(self, canvas) -> None:
        xCoordinates = [self.startPoint.x, self.endPoint.x]
        yCoordinates = [self.startPoint.y, self.endPoint.y]
        canvas.plot(xCoordinates, yCoordinates,
                    color = self.color,
                    linewidth = self.lineWidth)

    def __str__(self) -> str:
        return '{} -> {}'.format(self.startPoint, self.endPoint)