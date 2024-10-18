# Morph one shape into another interactively
# (can work in 3d too! see example warp4b.py)
#
from vedo import Plotter, Axes, dataurl, Assembly, printc, merge, Mesh
from vedo.shapes import Text2D, Points, Lines, Arrows2D, Grid
import os
import pickle

from morpher import Morpher

######################################################################################## MAIN
if __name__ == "__main__":
    
    a, b = 3, 5
    mesh0 = Mesh(os.path.join("splines", "image-0.vtk")).scale(0.01)
    mesha = Mesh(os.path.join("splines", f"image-{a}.vtk")).scale(0.01)
    meshb = Mesh(os.path.join("splines", f"image-{b}.vtk")).scale(0.01)
    
    mesha.align_to(mesh0, rigid=True)
    meshb.align_to(mesh0, rigid=True)
    morpher = Morpher(mesha, meshb, 10)
    morpher.load_points('morpher_points-b.pkl')
    morpher.n = 10
    morpher.start()
    # morpher.save_points('morpher_points.pkl')
    

    for i, mesh in enumerate(morpher.intermidiates): 
        fpath = os.path.join("intermidiates-b", f"{a}-{b}-{i}.vtk")
        mesh.write(fpath)

