from vedo import dataurl, Image, Mesh, Line, show
from vedo.applications import SplinePlotter  # ready to use class!
import sys
import os

# Read the input
if len(sys.argv) == 2:
    filename = sys.argv[1]
else:
    filename = "image.png"
filepath = os.path.join("images", filename)
pic = Image(filepath)

lineout = os.path.join("splines", filename.replace(".png", ".vtk"))
print(lineout)
print(os.path.exists(lineout))
if os.path.exists(lineout):
    line = Mesh(lineout)
    show(pic, line)
    sys.exit()


plt = SplinePlotter(pic)
plt.show(mode="image", zoom='tightest')

if plt.line:
    print("Npts =", len(plt.points()), "NSpline =", plt.line.npoints)

lineout = os.path.join("splines", filename.replace(".png", ".vtk"))
plt.line.write(lineout)
