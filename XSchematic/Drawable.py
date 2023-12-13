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
                 pointList: list[Point],
                 color : str = 'black',
                 lineWidth : float = 1.0) -> None:
        super().__init__()

        self.pointList = pointList
        self.color = color
        self.lineWidth = lineWidth
    
    def translate(self, translate : Point) -> Self:
        for index, point in enumerate(self.pointList):
            self.pointList[index] = point.translate(translate)
        return self
    
    def draw(self, canvas) -> None:
        xCoordinates = [ point.x for point in self.pointList ] 
        yCoordinates = [ point.y for point in self.pointList ]
        canvas.plot(xCoordinates, yCoordinates,
                    color = self.color,
                    linewidth = self.lineWidth)

    def __str__(self) -> str:
        return '{} -> {}'.format(self.startPoint, self.endPoint)