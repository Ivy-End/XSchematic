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
    
    def getBoundingBox(self) -> list:
        for drawable in self.drawables:
            for point in drawable.pointList:
                if self.boundingBox is None:
                    self.boundingBox = [ point.y, point.y, point.x, point.x ]
                else:
                    self.boundingBox[0] = max(self.boundingBox[0], point.y)
                    self.boundingBox[1] = min(self.boundingBox[1], point.y)
                    self.boundingBox[2] = min(self.boundingBox[2], point.x)
                    self.boundingBox[3] = max(self.boundingBox[3], point.x)
        return self.boundingBox
    
    def north(self) -> Point:
        self.getBoundingBox()
        return Point((self.boundingBox[2] + self.boundingBox[3]) / 2, self.boundingBox[0])

    def south(self) -> Point:
        self.getBoundingBox()
        return Point((self.boundingBox[2] + self.boundingBox[3]) / 2, self.boundingBox[1])
    
    def west(self) -> Point:
        self.getBoundingBox()
        return Point(self.boundingBox[2], (self.boundingBox[0] + self.boundingBox[1]) / 2)
    
    def east(self) -> Point:
        self.getBoundingBox()
        return Point(self.boundingBox[3], (self.boundingBox[0] + self.boundingBox[1]) / 2)
    
    def northWest(self) -> Point:
        self.getBoundingBox()
        return Point(self.boundingBox[2], self.boundingBox[0])
    
    def northEast(self) -> Point:
        self.getBoundingBox()
        return Point(self.boundingBox[3], self.boundingBox[0])
    
    def southWest(self) -> Point:
        self.getBoundingBox()
        return Point(self.boundingBox[2], self.boundingBox[1])
    
    def southEast(self) -> Point:
        self.getBoundingBox()
        return Point(self.boundingBox[3], self.boundingBox[1])

    def draw(self, canvas) -> None:
        for drawable in self.drawables:
            drawable.draw(canvas)
    
    def translate(self, point : Point) -> Self:
        for drawable in self.drawables:
            drawable.translate(point)
        return self

class Schematic:
    def __init__(self) -> None:
        self.instances = []
        self.properties = {}
        self.boundingBox = None

    def addInstance(self, instance: Symbol) -> Self:
        self.instances.append(instance)
        return self
    
    def __iadd__(self, instance: Symbol) -> Self:
        return self.addInstance(instance)
    
    def __enter__(self) -> Self:
        return self

    def __exit__(self, exc_type, exc_value, traceback) -> None:
        if exc_type is not None:
            print(exc_type, exc_value, traceback, sep = '\n')
    
    def getBoundingBox(self) -> list:
        for instance in self.instances:
            if self.boundingBox is None:
                self.boundingBox = instance.getBoundingBox()
            else:
                self.boundingBox[0] = max(self.boundingBox[0], instance.getBoundingBox()[0])
                self.boundingBox[1] = min(self.boundingBox[1], instance.getBoundingBox()[1])
                self.boundingBox[2] = min(self.boundingBox[2], instance.getBoundingBox()[2])
                self.boundingBox[3] = max(self.boundingBox[3], instance.getBoundingBox()[3])
        return self.boundingBox
    
    def draw(self, canvas) -> None:
        for instance in self.instances:
            instance.draw(canvas)
    
# class CellView:
#     def __init__(self, schematic = None, symbol = None, drawSchematic = False) -> None:
#         self.schematic = Schematic() if schematic == None else schematic
#         self.symbol = Symbol() if symbol == None else symbol
#         self.drawSchematic = drawSchematic
    
#     def setSchematic(self, schematic: Schematic) -> Self:
#         self.schematic = schematic
#         return self

#     def setSymbol(self, symbol: Symbol) -> Self:
#         self.symbol = symbol
#         return self
    
#     def draw(self, canvas) -> None:
#         if self.drawSchematic:
#             self.schematic.draw(canvas)
#         else:
#             self.symbol.draw(canvas)

#     def __str__(self) -> str:
#         if self.drawSchematic:
#             return str(self.schematic)
#         else:
#             return str(self.symbol)