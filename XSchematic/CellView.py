from typing import Self
from .Utility import Point
from .Drawable import Drawable

class Symbol:
    def __init__(self) -> None:
        self.drawables = []
    
    def addDrawable(self, drawable: Drawable) -> Self:
        self.drawables.append(drawable)
        return self

    def draw(self, canvas) -> None:
        for drawable in self.drawables:
            drawable.draw(canvas)

class Schematic:
    def __init__(self) -> None:
        self.instances = []

    def addInstance(self, instance: Symbol) -> Self:
        self.instances.append(instance)
        return self
    
    def draw(self, canvas) -> None:
        pass

class CellView:
    def __init__(self) -> None:
        self.schematic = None
        self.symbol = None

    def addInstance(self, instance: Self) -> Self:
        if self.schematic is None:
            self.schematic = Schematic()
        
        self.schematic.addInstance(instance)
    
    def draw(self, canvas) -> None:
        if self.schematic is not None:
            self.schematic.draw(canvas)
        else:
            self.symbol.draw(canvas)            

    def __str__(self) -> str:
        pass