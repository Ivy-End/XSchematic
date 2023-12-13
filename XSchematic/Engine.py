from abc import abstractmethod
from math import ceil, floor
from .CellView import Schematic
from .Utility import Point

import matplotlib.pyplot as plt

class Engine:
    def __init__(self) -> None:
        pass
        # self.margin = 1

class MatPlotLib(Engine):
    def __init__(self) -> None:
        super().__init__()

        self.canvas = plt
    
    # def setMargin(self, margin : float) -> None:
    #     self.margin = margin
    
    def draw(self, schematic : Schematic, debug = False) -> None:
        schematic.draw(self.canvas)

        #boundingBox = schematic.getBoundingBox()
        #for index, value in enumerate(boundingBox):
        #    boundingBox[index] = ceil(value) if value >= 0 else floor(value)
        #centerPoint = Point((boundingBox[2] + boundingBox[3]) / 2, (boundingBox[0] + boundingBox[1]) / 2)
        #canvasSize = max(boundingBox[3] - boundingBox[2], boundingBox[0] - boundingBox[1]) + 2 * self.margin
        #self.canvas.xlim(centerPoint.x - canvasSize / 2, centerPoint.x + canvasSize / 2)
        #self.canvas.ylim(centerPoint.y - canvasSize / 2, centerPoint.y + canvasSize / 2)
        self.canvas.gca().set_aspect('equal', adjustable = 'box')

        if debug:
            self.canvas.grid(visible = True, which = 'both', axis = 'both', color = 'DeepSkyBlue', linestyle = '-.', linewidth = 0.5)
            #self.canvas.gcf().set_figwidth(canvasSize)
            #self.canvas.gcf().set_figheight(canvasSize)
            #print('The center point of the canvas is: {}'.format(centerPoint))
            #print('The size of the canvas is: {}'.format(canvasSize))
    
    def show(self) -> None:
        self.canvas.show()
    
    def save(self, fname) -> None:
        self.canvas.axis('off')
        self.canvas.savefig(fname, bbox_inches = 'tight', pad_inches = 0)
        self.canvas.axis('on')