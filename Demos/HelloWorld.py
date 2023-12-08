import sys
sys.path.append(".")

import XSchematic
import XSchematic.Element
import XSchematic.Engine
import XSchematic.Utility

import matplotlib.pyplot as plt

from XSchematic.Utility import Point


if __name__ == "__main__":
    element = XSchematic.Element.Line(Point(0, 0), Point(1, 1))
    engine = XSchematic.Engine.MatPlotLib()
    engine.draw(element)
    engine.show()