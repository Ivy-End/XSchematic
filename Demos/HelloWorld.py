import sys
sys.path.append(".")

import XSchematic
import XSchematic.Element
import XSchematic.Engine
import XSchematic.Utility

import matplotlib.pyplot as plt

from XSchematic.Utility import Point


if __name__ == "__main__":
    element_1 = XSchematic.Element.PolyLine(
        [
            XSchematic.Element.Line(Point(0, 0), Point(1, 1)), 
            XSchematic.Element.Line(Point(1, 1), Point(2, 1)), 
            XSchematic.Element.Line(Point(2, 1), Point(1, 2)), 
            XSchematic.Element.Line(Point(1, 2), Point(0, 0))
        ])
    engine = XSchematic.Engine.MatPlotLib()

    engine.draw(element_1)
    engine.show()