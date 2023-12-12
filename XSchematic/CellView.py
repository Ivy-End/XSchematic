from abc import abstractmethod
from typing import Self
from .Utility import Point
from .Drawable import Drawable

class Symbol:
    def __init__(self) -> None:
        self.drawables = []
        self.boundingBox = None # [ N, S, W, E ]
    
    def addDrawable(self, drawable: Drawable) -> Self:
        self.drawables.append(drawable)
        
        for point in drawable.pointList:
            if self.boundingBox is None:
                self.boundingBox = [ point.y, point.y, point.x, point.x ]
            else:
                self.boundingBox[0] = max(self.boundingBox[0], point.y)
                self.boundingBox[1] = min(self.boundingBox[1], point.y)
                self.boundingBox[2] = min(self.boundingBox[2], point.x)
                self.boundingBox[3] = max(self.boundingBox[3], point.x)

        return self

    def draw(self, canvas, properties) -> None:
        for drawable in self.drawables:
            drawable.draw(canvas)
    
    def origin(self) -> Point:
        return Point(0, 0)
        
    def north(self) -> Point:
        return Point((self.boundingBox[2] + self.boundingBox[3]) / 2, self.boundingBox[0])
    
    def south(self) -> Point:
        return Point((self.boundingBox[2] + self.boundingBox[3]) / 2, self.boundingBox[1])
    
    def west(self) -> Point:
        return Point(self.boundingBox[2], (self.boundingBox[0] + self.boundingBox[1]) / 2)
    
    def east(self) -> Point:
        return Point(self.boundingBox[3], (self.boundingBox[0] + self.boundingBox[1]) / 2)
    
    def northWest(self) -> Point:
        return Point(self.boundingBox[2], self.boundingBox[0])
    
    def northEast(self) -> Point:
        return Point(self.boundingBox[3], self.boundingBox[0])
    
    def southWest(self) -> Point:
        return Point(self.boundingBox[2], self.boundingBox[1])
    
    def southEast(self) -> Point:
        return Point(self.boundingBox[3], self.boundingBox[1])
    
    @abstractmethod
    def center(self) -> Point:
        return NotImplemented
    
    @abstractmethod
    def left(self) -> Point:
        return NotImplemented
    
    @abstractmethod
    def right(self) -> Point:
        return NotImplemented

class Schematic:
    def __init__(self) -> None:
        self.instances = []
        self.properties = {}

    def addInstance(self, instance: Symbol) -> Self:
        self.instances.append(instance)
        return self
    
    def draw(self, canvas) -> None:
        for instance in self.instances:
            instance.draw(canvas, self.properties)
    
class CellView:
    def __init__(self, drawSchematic = False) -> None:
        self.schematic = Schematic()
        self.symbol = Symbol()
        self.drawSchematic = drawSchematic
    
    def draw(self, canvas) -> None:
        if self.drawSchematic:
            self.schematic.draw(canvas)
        else:
            self.symbol.draw(canvas)

    def __str__(self) -> str:
        if self.drawSchematic:
            return str(self.schematic)
        else:
            return str(self.symbol)