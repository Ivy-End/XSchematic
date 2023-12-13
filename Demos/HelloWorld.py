import sys
sys.path.append(".")

from XSchematic import CellView, Drawable, Engine, Utility
from XSchematic.SDK import Ground

if __name__ == "__main__":
    engine = Engine.MatPlotLib()

    with CellView.Schematic() as sch:
        sch += (ground := Ground.Ground().translate(point = Utility.Point(0, 0)))
        sch += (tlground := Ground.TaillessGround().translate(point = Utility.Point(2, 0)))
        sch += (refground := Ground.ReferenceGround().translate(point = Utility.Point(4, 0)))

        engine.draw(sch, debug = True)
        
    engine.save("test.svg")
    engine.show()