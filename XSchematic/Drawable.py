from abc import abstractmethod
from typing import Self
from .Utility import Point

class Drawable:
    def __init__(self) -> None:
        pass
    
    @abstractmethod
    def translate(self, translate : Point) -> Self:
        raise NotImplemented

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
                 lineWidth : float = 1.0,
                 solidCapStyle : str = 'round') -> None:

        self.pointList = pointList
        self.color = color
        self.lineWidth = lineWidth
        self.solidCapStyle = solidCapStyle

    def translate(self, translate : Point) -> Self:
        for index, point in enumerate(self.pointList):
            self.pointList[index] = point.translate(translate)
        return self
    
    def draw(self, canvas) -> None:
        xCoordinates = [ point.x for point in self.pointList ] 
        yCoordinates = [ point.y for point in self.pointList ]
        canvas.plot(xCoordinates, yCoordinates,
                    color = self.color,
                    linewidth = self.lineWidth,
                    solid_capstyle = self.solidCapStyle)

    def __str__(self) -> str:
        return '{} -> {}'.format(self.startPoint, self.endPoint)

class PolyLine(Drawable):
    def __init__(self, 
                 pointList: list[Point],
                 edgeColor : str = 'black',
                 faceColor : str = 'lightskyblue',
                 lineWidth : float = 1.0,
                 joinStyle : str = 'round') -> None:

        self.pointList = pointList
        self.edgeColor = edgeColor
        self.faceColor = faceColor
        self.lineWidth = lineWidth
        self.joinStyle = joinStyle

    def translate(self, translate : Point) -> Self:
        for index, point in enumerate(self.pointList):
            self.pointList[index] = point.translate(translate)
        return self
    
    def draw(self, canvas) -> None:
        xCoordinates = [ point.x for point in self.pointList ] + [ self.pointList[0].x ]
        yCoordinates = [ point.y for point in self.pointList ] + [ self.pointList[0].y ]
        canvas.fill(xCoordinates, yCoordinates,
                    edgecolor = self.edgeColor,
                    facecolor = self.faceColor,
                    linewidth = self.lineWidth,
                    joinstyle = self.joinStyle)

    def __str__(self) -> str:
        return '{} -> {}'.format(self.startPoint, self.endPoint)