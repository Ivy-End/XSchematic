from ..Drawable import *
from ..Utility import *
from ..CellView import CellView, Symbol

class Ground(CellView):
    def __init__(self):
        super().__init__()

        self.symbol = self.buildSymbol()
    
    def buildSymbol(self):
        symbol = Symbol()

        symbol.addDrawable(Line(Point(0, 0), Point(0, -1.2)))
        symbol.addDrawable(Line(Point(-0.6, -1.2), Point(0.6, -1.2), lineWidth = 2))
        symbol.addDrawable(Line(Point(-0.4, -1.4), Point(0.4, -1.4), lineWidth = 2))
        symbol.addDrawable(Line(Point(-0.25, -1.6), Point(0.25, -1.6), lineWidth = 2))
        
        return symbol