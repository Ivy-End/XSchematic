from abc import abstractmethod
from typing import Self
from .Utility import Point
from .Drawable import Drawable

class Symbol:
    def __init__(self) -> None:
        self.__drawables = []
        self.__boundingBox = None # [ N, S, W, E ]
    
    def addDrawable(self, drawable: Drawable) -> Self:
        self.__drawables.append(drawable)
    
    def getBoundingBox(self) -> list:
        for drawable in self.__drawables:
            for point in drawable.pointList:
                if self.__boundingBox is None:
                    self.__boundingBox = [ point.y, point.y, point.x, point.x ]
                else:
                    self.__boundingBox[0] = max(self.__boundingBox[0], point.y)
                    self.__boundingBox[1] = min(self.__boundingBox[1], point.y)
                    self.__boundingBox[2] = min(self.__boundingBox[2], point.x)
                    self.__boundingBox[3] = max(self.__boundingBox[3], point.x)
        return self.__boundingBox
    
    def north(self) -> Point:
        self.getBoundingBox()
        return Point((self.__boundingBox[2] + self.__boundingBox[3]) / 2, self.__boundingBox[0])

    def south(self) -> Point:
        self.getBoundingBox()
        return Point((self.__boundingBox[2] + self.__boundingBox[3]) / 2, self.__boundingBox[1])
    
    def west(self) -> Point:
        self.getBoundingBox()
        return Point(self.__boundingBox[2], (self.__boundingBox[0] + self.__boundingBox[1]) / 2)
    
    def east(self) -> Point:
        self.getBoundingBox()
        return Point(self.__boundingBox[3], (self.__boundingBox[0] + self.__boundingBox[1]) / 2)
    
    def northWest(self) -> Point:
        self.getBoundingBox()
        return Point(self.__boundingBox[2], self.__boundingBox[0])
    
    def northEast(self) -> Point:
        self.getBoundingBox()
        return Point(self.__boundingBox[3], self.__boundingBox[0])
    
    def southWest(self) -> Point:
        self.getBoundingBox()
        return Point(self.__boundingBox[2], self.__boundingBox[1])
    
    def southEast(self) -> Point:
        self.getBoundingBox()
        return Point(self.__boundingBox[3], self.__boundingBox[1])

    def center(self) -> Point:
        self.getBoundingBox()
        return Point((self.__boundingBox[2] + self.__boundingBox[3]) / 2, (self.__boundingBox[0] + self.__boundingBox[1]) / 2)

    def draw(self, canvas) -> None:
        for drawable in self.__drawables:
            drawable.draw(canvas)
    
    def translate(self, point : Point) -> Self:
        for drawable in self.__drawables:
            drawable.translate(point)
        return self

class Schematic:
    def __init__(self) -> None:
        self.__instances = []
        self.__boundingBox = None

    def addInstance(self, instance: Symbol) -> Self:
        self.__instances.append(instance)
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
            if self.__boundingBox is None:
                self.__boundingBox = instance.getBoundingBox()
            else:
                self.__boundingBox[0] = max(self.__boundingBox[0], instance.getBoundingBox()[0])
                self.__boundingBox[1] = min(self.__boundingBox[1], instance.getBoundingBox()[1])
                self.__boundingBox[2] = min(self.__boundingBox[2], instance.getBoundingBox()[2])
                self.__boundingBox[3] = max(self.__boundingBox[3], instance.getBoundingBox()[3])
        return self.__boundingBox
    
    def draw(self, canvas) -> None:
        for instance in self.__instances:
            instance.draw(canvas)