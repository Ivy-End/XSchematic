from ..Drawable import *
from ..Utility import *
from ..CellView import CellView, Symbol

class Ground(CellView):
    def __init__(self):
        super().__init__()

        self.symbol = self.buildSymbol()
    
    def buildSymbol(self):
        symbol = Symbol()

        symbol.addDrawable(Line(Point(0.5, 1), Point(0.5, 0)))
        symbol.addDrawable(Line(Point(0, 0), Point(1, 0)))
        symbol.addDrawable(Line(Point(0.2, -0.2), Point(0.8, -0.2)))
        symbol.addDrawable(Line(Point(0.4, -0.4), Point(0.6, -0.4)))
        
        return symbol