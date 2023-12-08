import sys
sys.path.append(".")

from XSchematic import CellView, Drawable, Engine, Utility
from XSchematic.SDK import Ground

if __name__ == "__main__":
    engine = Engine.MatPlotLib()

    cv = CellView.CellView()
    cv.addInstance(Ground.Ground())
    #engine.draw(cv)
    g = Ground.Ground()
    engine.draw(g)

    engine.save("test.svg")
    engine.show()