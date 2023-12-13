from abc import abstractmethod
from ..Drawable import *
from ..Utility import *
from ..CellView import Symbol

class AbstractGround(Symbol):
    def __init__(self, scale = 0.35, lineWidthConnection = 1, lineWidth = 2) -> None:
        super().__init__()
        
        self.scale = scale
        self.lineWidthConnection = lineWidthConnection
        self.lineWidth = lineWidth
        self.scale = scale

        self.buildSymbol()

    @abstractmethod
    def buildSymbol(self) -> None:
        raise NotImplemented
    
    def pinGround(self) -> Point:
        return self.north()

    def setProperties(self, **kwargs) -> None:
        if 'scale' in kwargs:
            self.scale = kwargs['scale']
        if 'lineWidthConnection' in kwargs:
            self.lineWidthConnection = kwargs['lineWidthConnection']
        if 'lineWidth' in kwargs:
            self.lineWidth = kwargs['lineWidth']


class Ground(AbstractGround):
    def buildSymbol(self) -> None:
        self.drawables.append(Line(pointList = [Point( 0                ,  0               ),
                                                Point( 0                , -1.2 * self.scale)], lineWidth = self.lineWidthConnection))
        self.drawables.append(Line(pointList = [Point(-0.6  * self.scale, -1.2 * self.scale),
                                                Point( 0.6  * self.scale, -1.2 * self.scale)], lineWidth = self.lineWidth))
        self.drawables.append(Line(pointList = [Point(-0.4  * self.scale, -1.4 * self.scale),
                                                Point( 0.4  * self.scale, -1.4 * self.scale)], lineWidth = self.lineWidth))
        self.drawables.append(Line(pointList = [Point(-0.25 * self.scale, -1.6 * self.scale),
                                                Point( 0.25 * self.scale, -1.6 * self.scale)], lineWidth = self.lineWidth))

class TaillessGround(AbstractGround):
    def buildSymbol(self) -> None:
        self.drawables.append(Line(pointList = [Point(-0.6  * self.scale,  0               ),
                                                Point( 0.6  * self.scale,  0               )], lineWidth = self.lineWidth))
        self.drawables.append(Line(pointList = [Point(-0.4  * self.scale, -0.2 * self.scale),
                                                Point( 0.4  * self.scale, -0.2 * self.scale)], lineWidth = self.lineWidth))
        self.drawables.append(Line(pointList = [Point(-0.25 * self.scale, -0.4 * self.scale),
                                                Point( 0.25 * self.scale, -0.4 * self.scale)], lineWidth = self.lineWidth))

class ReferenceGround(AbstractGround):
    def buildSymbol(self) -> None:    
        self.drawables.append(Line(pointList = [Point( 0               ,  0             ),
                                                Point( 0               , -1 * self.scale)], lineWidth = self.lineWidthConnection))
        self.drawables.append(Line(pointList = [Point(-0.6 * self.scale, -1 * self.scale),
                                                Point( 0.6 * self.scale, -1 * self.scale)], lineWidth = self.lineWidth))

class SignalGround(AbstractGround):
    def buildSymbol(self) -> None:
        super(SignalGround, self).setProperties(lineWidth = 3)

        self.drawables.append(    Line(pointList = [Point( 0               ,  0               ),
                                                    Point( 0               , -1   * self.scale)], lineWidth = self.lineWidthConnection))
        self.drawables.append(PolyLine(pointList = [Point(-0.6 * self.scale, -1   * self.scale),
                                                    Point( 0.6 * self.scale, -1   * self.scale),
                                                    Point( 0               , -1.8 * self.scale)], lineWidth = self.lineWidth))

class ThickerGround(AbstractGround):
    def buildSymbol(self) -> None:
        super(ThickerGround, self).setProperties(lineWidth = 3)

        self.drawables.append(Line(pointList = [Point(-0.6 * self.scale, 0),
                                                Point( 0.6 * self.scale, 0)], lineWidth = self.lineWidth))

class NoiselessGround(AbstractGround):
    def buildSymbol(self) -> None:
        self.drawables.append(Line(pointList = [Point( 0               ,  0               ),
                                                Point( 0               , -1.2 * self.scale)], lineWidth = self.lineWidthConnection))
        self.drawables.append(Line(pointList = [Point(-0.6 * self.scale, -1.2 * self.scale),
                                                Point( 0.6 * self.scale, -1.2 * self.scale)], lineWidth = self.lineWidth))
        self.drawables.append(Line(pointList = [Point(-0.4 * self.scale, -1.4 * self.scale),
                                                Point( 0.4 * self.scale, -1.4 * self.scale)], lineWidth = self.lineWidth))
        self.drawables.append(Line(pointList = [Point(-0.25 * self.scale, -1.6 * self.scale),
                                                Point( 0.25 * self.scale, -1.6 * self.scale)], lineWidth = self.lineWidth))
        self.drawables.append(Arc(startAngle = 0, endAngle = 180, center = Point(0.9 * self.scale, -1.6 * self.scale), radius = 0.9 * self.scale, lineWidth = self.lineWidth))