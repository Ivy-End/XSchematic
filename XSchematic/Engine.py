from abc import abstractmethod
from .CellView import CellView

import matplotlib.pyplot as plt

class Engine:
    def __init__(self) -> None:
        pass

class MatPlotLib(Engine):
    def __init__(self) -> None:
        super().__init__()

        self.canvas = plt
    
    def draw(self, cellView : CellView) -> None:
        cellView.draw(self.canvas)
    
    def show(self) -> None:
        self.canvas.show()
    
    def save(self, fname) -> None:
        self.canvas.axis('off')
        self.canvas.savefig(fname, bbox_inches = 'tight', pad_inches = 0)
        self.canvas.axis('on')