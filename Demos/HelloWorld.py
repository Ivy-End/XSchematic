import sys
sys.path.append(".")

from XSchematic import CellView, Drawable, Engine, Utility
from XSchematic.SDK import Ground

if __name__ == "__main__":
    engine = Engine.MatPlotLib()

    cv = CellView.CellView(drawSchematic = True)
    cv.schematic.addInstance(Ground.Ground())
    engine.draw(cv)

    engine.save("test.svg")
    engine.show()