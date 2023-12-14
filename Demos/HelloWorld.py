import sys
sys.path.append(".")

from XSchematic import CellView, Drawable, Engine, Utility
from XSchematic.SDK import Ground

if __name__ == "__main__":
    engine = Engine.MatPlotLib()

    with CellView.Schematic() as sch:
        sch += (ground := Ground.Ground().translate(point = Utility.Point(0, 0) - Ground.Ground().center()))
        sch += (tlground := Ground.TaillessGround().translate(point = Utility.Point(1, 0) - Ground.TaillessGround().center()))
        sch += (refground := Ground.ReferenceGround().translate(point = Utility.Point(2, 0) - Ground.ReferenceGround().center()))
        sch += (sground := Ground.SignalGround().translate(point = Utility.Point(3, 0) - Ground.SignalGround().center()))
        sch += (tground := Ground.ThickerGround().translate(point = Utility.Point(4, 0) - Ground.ThickerGround().center()))
        sch += (nground := Ground.NoiselessGround().translate(point = Utility.Point(5, 0) - Ground.NoiselessGround().center()))
        sch += (pground := Ground.ProtectiveGround().translate(point = Utility.Point(6, 0) - Ground.ProtectiveGround().center()))
        sch += (cground := Ground.ChassisGround().translate(point = Utility.Point(7, 0) - Ground.ChassisGround().center()))
        sch += (eground := Ground.EuropeanStyleGround().translate(point = Utility.Point(8, 0) - Ground.EuropeanStyleGround().center()))
        sch += (eground2 := Ground.EuropeanStyleGround2().translate(point = Utility.Point(9, 0) - Ground.EuropeanStyleGround2().center()))

        engine.draw(sch, debug = True)
        
    engine.save("test.png")
    engine.show()