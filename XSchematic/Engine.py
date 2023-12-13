from abc import abstractmethod
from math import ceil, floor
from .CellView import Schematic
from .Utility import Point

import matplotlib.pyplot as plt

class Engine:
    def __init__(self) -> None:
        pass

class MatPlotLib(Engine):
    def __init__(self) -> None:
        super().__init__()

        self.__canvas = plt
    
    def draw(self, schematic : Schematic, debug = False) -> None:
        schematic.draw(self.__canvas)
        self.__canvas.gca().set_aspect('equal', adjustable = 'box')

        if debug:
            self.__canvas.grid(visible = True, which = 'both', axis = 'both', color = 'DeepSkyBlue', linestyle = '-.', linewidth = 0.5)
    
    def show(self) -> None:
        self.__canvas.show()
    
    def save(self, fname) -> None:
        self.__canvas.axis('off')
        self.__canvas.savefig(fname, bbox_inches = 'tight', pad_inches = 0)
        self.__canvas.axis('on')