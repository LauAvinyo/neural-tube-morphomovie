"""Colorize a mesh cell by clicking on it"""
from vedo import Mesh, Plotter, dataurl, np, Plane
import os
import vedo
import sys

vedo.settings.enable_default_mouse_callbacks

def normalize(v):
    return (v - v.min()) / (v.max() - v.min())

global value, m, radious, square, new_values
radious = 0.2
value = 0


def pos2coordinate(pos):
    # TODO: Fix this! 
    # print(pos)
    try:
        a, b, _ = np.array(pos) 
    except:
        a, b = 0, 0
    return a, b


folder = "hoxa7"

def func(evt):
    global value, m, square, new_values
    m = evt.object
    if not m:
        return
    pt = evt.picked3d
    idcell = m.closest_point(pt, return_cell_id=True)

    if evt.keypress == "c":
        value = m.celldata["expression"][idcell]
        print("Capturing value!", value)
    else:
        print("We setting value")
        cc = m.cell_centers 
        # print(cc)
        print(cc.shape)
        a, b = pos2coordinate(pt)
        c1 = np.logical_and(cc[:, 0] < (a + radious), (a - radious) < cc[:, 0])
        c2 = np.logical_and(cc[:, 1] < (b + radious), (b - radious) < cc[:, 1])
        ix = np.logical_and(c1, c2)
        current = m.celldata["expression"][ix].mean()
        change = (value - current) * 0.2
        # exit()

        # # idx = (a - radious) < cc[:, 1] < (a + radious)
        m.celldata["expression"][ix] += change
        new_values = m.celldata["expression"]
        m.cmap("viridis", "expression" , on="cells")

def brush_size(evt):
    global square, plt

    pos = evt.picked3d
    a, b = pos2coordinate(pos)
    plt.remove(square)
    square = Plane((a, b, -1), s=[radious*2, radious*2]).linewidth(10)
    plt.add(square)
    plt.render()


square = Plane((0, 0, -1), s=[radious*2, radious*2]).opacity(1).linewidth(10)
# Load a 3D mesh of a panther from a file and set its color to blue
file = os.path.join(folder, sys.argv[1])


m = Mesh(file).opacity(0.9)
m.compute_normals()
values = m.pointdata["RGBA"]
values = normalize(values)
values = 1 - values
m.pointdata["expression"] = values
m.smooth_data()
m.map_points_to_cells()
values = m.celldata["expression"]
new_values = values
m.cmap("viridis", "expression" , on="cells")

# # Make the mesh opaque and set its line width to 1
# m.force_opaque().linewidth(1)

# Create a Plotter object and add the callback function to it
plt = Plotter()
plt.remove_all_observers()
plt.add_callback("mouse click", func)
plt.add_callback("mouse move", brush_size)



# Display the mesh with the Plotter object and the docstring
plt.show(m, square, __doc__, axes=1).close()
new_values[new_values > 1] = 1
m.celldata["clean_expression"] = new_values
m.smooth_data()
m.write(file.replace(".vtk", "_clean.vtk"))
# m.write(file)