from ..Drawable import *
from ..Utility import *
from ..CellView import Symbol

class Ground(Symbol):
    def __init__(self, sizeCoeff = 1.0) -> None:
        super().__init__()

        self.drawables.append(Line([ Point(0, 0), Point(0, -1.2) ]))
        self.drawables.append(Line([ Point(-0.6, -1.2), Point(0.6, -1.2) ], lineWidth = 2))
        self.drawables.append(Line([ Point(-0.4, -1.4), Point(0.4, -1.4) ], lineWidth = 2))
        self.drawables.append(Line([ Point(-0.25, -1.6), Point(0.25, -1.6) ], lineWidth = 2))

class TaillessGround(Symbol):
    def __init__(self) -> None:
        super().__init__()
        
        self.drawables.append(Line([ Point(-0.6, 0), Point(0.6, 0) ], lineWidth = 2))
        self.drawables.append(Line([ Point(-0.4, -0.2), Point(0.4, -0.2) ], lineWidth = 2))
        self.drawables.append(Line([ Point(-0.25, -0.4), Point(0.25, -0.4) ], lineWidth = 2))

class ReferenceGround(Symbol):
    def __init__(self) -> None:
        super().__init__()
        
        self.drawables.append(Line([ Point(0, 0), Point(0, -1.4 / 4) ], lineWidth = 2))
        self.drawables.append(Line([ Point(-0.6 * 1.4 / 4, -1.4 / 4), Point(0.6 * 1.4 / 4, -1.4 / 4) ], lineWidth = 2))