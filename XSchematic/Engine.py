from abc import abstractmethod
from .Element import Line

import matplotlib.pyplot as plt

class Engine:
    def __init__(self):
        pass

class MatPlotLib(Engine):
    def __init__(self):
        super().__init__()

        self.canvas = plt
    
    def draw(self, line: Line):
        line.draw(self.canvas)
    
    def show(self):
        self.canvas.show()
    
    def save(self, fname):
        self.canvas.axis('off')
        self.canvas.savefig(fname, bbox_inches = 'tight', pad_inches = 0)
        self.canvas.axis('on')