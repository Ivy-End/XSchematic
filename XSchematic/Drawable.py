from abc import abstractmethod
from typing import Self
from .Utility import Point
import numpy as np

class Drawable:
    def __init__(self,
                 # Line/Polygon
                 pointList : list[Point] = [],
                 # Arc
                 startAngle : float = 0.0,
                 endAngle : float = 360.0,
                 angleResolution : float = 0.1,
                 center : Point = None,
                 radius : float = None,
                 ratio : float = 1.0,
                 # Common
                 fill : bool = False,
                 lineWidth : float = 1.0,
                 edgeColor : str = 'black',
                 fillColor : str = 'lightskyblue',
                 capStyle : str = 'round',
                 joinStyle : str = 'round') -> None:

        self.pointList = pointList
        self.startAngle = startAngle
        self.endAngle = endAngle
        self.angleResolution = angleResolution
        self.center = center
        self.radius = radius
        self.ratio = ratio
        
        self.fill = fill
        self.lineWidth = lineWidth
        self.edgeColor = edgeColor
        self.fillColor = fillColor
        self.capStyle = capStyle
        self.joinStyle = joinStyle

        self.buildDrawable()

    def buildDrawable(self) -> None:
        pass

    def draw(self, canvas) -> None:
        xCoordinates = [ point.x for point in self.pointList ] 
        yCoordinates = [ point.y for point in self.pointList ]
        if not self.fill:
            canvas.plot(xCoordinates, yCoordinates,
                        color = self.edgeColor,
                        linewidth = self.lineWidth,
                        solid_capstyle = self.capStyle,
                        solid_joinstyle = self.joinStyle,
                        dash_capstyle = self.capStyle,
                        dash_joinstyle = self.joinStyle)
        else:
            canvas.fill(xCoordinates, yCoordinates,
                        edgecolor = self.edgeColor,
                        facecolor = self.fillColor,
                        linewidth = self.lineWidth,
                        capstyle = self.capStyle,
                        joinstyle = self.joinStyle)
    
    def setProperties(self, **kwargs) -> None:
        if 'pointList' in kwargs:
            self.pointList = kwargs['pointList']
        if 'startAngle' in kwargs:
            self.startAngle = kwargs['startAngle']
        if 'endAngle' in kwargs:
            self.endAngle = kwargs['endAngle']
        if 'angleResolution' in kwargs:
            self.angleResolution = kwargs['angleResolution']
        if 'center' in kwargs:
            self.center = kwargs['center']
        if 'radius' in kwargs:
            self.radius = kwargs['radius']
        if 'fill' in kwargs:
            self.fill = kwargs['fill']
        if 'lineWidth' in kwargs:
            self.lineWidth = kwargs['lineWidth']
        if 'edgeColor' in kwargs:
            self.edgeColor = kwargs['edgeColor']
        if 'fillColor' in kwargs:
            self.fillColor = kwargs['fillColor']
        if 'capStyle' in kwargs:
            self.capStyle = kwargs['capStyle']
        if 'joinStyle' in kwargs:
            self.joinStyle = kwargs['joinStyle']

    def translate(self, translate : Point) -> Self:
        if self.pointList is not None:
            for index, point in enumerate(self.pointList):
                self.pointList[index] = point.translate(translate)
            return self

        
class Line(Drawable):
    pass

class Polygon(Drawable):
    def buildDrawable(self) -> None:
        super().setProperties(fill = True)
        self.pointList.append(self.pointList[0])
        
class Arc(Drawable):
    def buildDrawable(self) -> None:
        for angle in np.arange(self.startAngle, self.endAngle, self.angleResolution):
            self.pointList.append(Point(self.center.x + self.radius * np.cos(np.deg2rad(angle)), self.center.y + self.radius * self.ratio * np.sin(np.deg2rad(angle))))
        self.pointList.append(Point(self.center.x + self.radius * np.cos(np.deg2rad(self.endAngle)), self.center.y + self.radius * self.ratio * np.sin(np.deg2rad(self.endAngle))))

class Ellipse(Drawable):
    def buildDrawable(self) -> None:
        super().setProperties(startAngle = 0, endAngle = 360, angleResolution = 0.1, fill = True)
        # for angle in np.arange(self.startAngle, self.endAngle, self.angleResolution):
        #     self.pointList.append(Point(self.center.x + self.radius * np.cos(np.deg2rad(angle)), self.center.y + self.radius * self.ratio * np.sin(np.deg2rad(angle))))