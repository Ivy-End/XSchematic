import sys
sys.path.append(".")

from XSchematic import CellView, Drawable, Engine, Utility
from XSchematic.SDK import Ground

if __name__ == "__main__":
    engine = Engine.MatPlotLib()

    with CellView.Schematic() as sch:
        sch += (ground := Ground.Ground())
        sch += (tlground := Ground.TaillessGround().translate(point = ground.northEast() + Utility.Point(0.5, 0)))
        sch += (refground := Ground.ReferenceGround().translate(point = tlground.northEast() + Utility.Point(0.5, 0)))
        sch += (sground := Ground.SignalGround().translate(point = refground.northEast() + Utility.Point(0.5, 0)))
        sch += (tground := Ground.ThickerGround().translate(point = sground.northEast() + Utility.Point(0.5, 0)))
        sch += (nground := Ground.NoiselessGround().translate(point = tground.northEast() + Utility.Point(0.5, 0)))
        sch += (pground := Ground.ProtectiveGround().translate(point = nground.northEast() + Utility.Point(0.5, 0)))
        sch += (cground := Ground.ChassisGround().translate(point = pground.northEast() + Utility.Point(0.5, 0)))
        sch += (eground := Ground.EuropeanStyleGround().translate(point = cground.northEast() + Utility.Point(1, 0)))
        sch += (eground2 := Ground.EuropeanStyleGround2().translate(point = eground.northEast() + Utility.Point(1, 0)))

        engine.draw(sch, debug = True)
        
    engine.save("test.png")
    engine.show()