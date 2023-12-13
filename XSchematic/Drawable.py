from abc import abstractmethod
from typing import Self
from .Utility import Point

class Drawable:
    def __init__(self,
                 # Line/PolyLine
                 pointList : list[Point] = None,
                 # Arc
                 startAngle : float = 0.0,
                 endAngle : float = 360.0,
                 center : Point = None,
                 radius : float = None,
                 # Common
                 lineWidth : float = 1.0,
                 edgeColor : str = 'black',
                 fillColor : str = 'lightskyblue',
                 capStyle : str = 'round',
                 joinStyle : str = 'round') -> None:
        self.pointList = pointList

        self.startAngle = startAngle
        self.endAngle = endAngle
        self.center = center
        self.radius = radius

        self.lineWidth = lineWidth
        self.edgeColor = edgeColor
        self.fillColor = fillColor
        self.capStyle = capStyle
        self.joinStyle = joinStyle
    
    def translate(self, translate : Point) -> Self:
        if self.pointList is not None:
            for index, point in enumerate(self.pointList):
                self.pointList[index] = point.translate(translate)
            return self

    @abstractmethod
    def draw(self, canvas) -> None:
        raise NotImplemented

class Line(Drawable):
    def draw(self, canvas) -> None:
        xCoordinates = [ point.x for point in self.pointList ] 
        yCoordinates = [ point.y for point in self.pointList ]
        canvas.plot(xCoordinates, yCoordinates,
                    color = self.edgeColor,
                    linewidth = self.lineWidth,
                    solid_capstyle = self.capStyle,
                    solid_joinstyle = self.joinStyle,
                    dash_capstyle = self.capStyle,
                    dash_joinstyle = self.joinStyle)

class PolyLine(Drawable):
    def draw(self, canvas) -> None:
        xCoordinates = [ point.x for point in self.pointList ] + [ self.pointList[0].x ]
        yCoordinates = [ point.y for point in self.pointList ] + [ self.pointList[0].y ]
        canvas.fill(xCoordinates, yCoordinates,
                    edgecolor = self.edgeColor,
                    facecolor = self.fillColor,
                    linewidth = self.lineWidth,
                    capstyle = self.capStyle,
                    joinstyle = self.joinStyle)
        
class Arc(Drawable):
    def draw(self, canvas) -> None:
        # canvas.gca().add_patch(mat(xy = (self.center.x, self.center.y),
        #                                     width = self.radius * 2, height = self.radius * 2,
        #                                     theta1 = self.startAngle, theta2 = self.endAngle,
        #                                     edgecolor = self.edgeColor,
        #                                     linewidth = self.lineWidth,
        #                                     capstyle = self.capStyle,
        #                                     joinstyle = self.joinStyle))
        pass