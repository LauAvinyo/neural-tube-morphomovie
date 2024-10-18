from vedo.applications import Browser, SplinePlotter
from vedo import Mesh, Image, show, printc
import os
import sys
from morpher import Morpher

vis = []

cmap = "RdYlBu"


# Read the couse
mesh_id = 0
course = {}
for a, b in ((0, 3), (3, 5)):
    for r in range(11):
        p = os.path.join("intermidiates-b", f"{a}-{b}-{r}.vtk")
        if not os.path.exists(p):
            continue
        msh = Mesh(p).lw(4).c("k")
        course[mesh_id] = msh
        vis.append(msh)
        mesh_id  += 1


# Read the image and get the countour line. 
# Read the input
if len(sys.argv) == 2:
    filename = sys.argv[1]
else:
    filename = "image.png"
filepath = os.path.join("images", filename)
pic = Image(filepath)

# Check if the line has already been selected for this
lineout = os.path.join("splines", filename.replace(".png", ".vtk"))
if os.path.exists(lineout):
    spline = Mesh(lineout).scale(0.01)
    # show(pic, spline)
    # sys.exit()
else:
    # Align it with each of the contour. 
    plt = SplinePlotter(pic)
    plt.show(mode="image", zoom='tightest')
    spline = plt.line.scale(0.01)
    plt.close()

# printc("Staging...", c="green")
# differences = []
# for k in course:
#     c_spline = spline.clone()
#     c_spline.align_to(course[k], rigid=True)
#     distance = c_spline.distance_to(course[k], signed=False)
#     differences.append((distance.mean(), k))

# differences = sorted(differences)
# d, k = differences[0]
d, k = 0, 9
spline.align_to(course[k])
print(f"{k} with distance {d}")
# show(
#     spline, 
#     pic.apply_transform(spline.transform), 
#     course[k]
# )

# Map the gene expression
pic_mesh = pic.tomesh()
pic_mesh.apply_transform(spline.transform)

printc("Cutting using outline... (please wait)", c="g6")
cut_msh = pic_mesh.clone().cut_with_point_loop(spline)
cut_msh.pointdata.select("RGBA")
cut_msh.add_scalarbar3d("Expression level")
cut_msh.smooth().decimate(0.1).smooth()
# exit()

# msh = spline.generate_mesh().smooth()
# msh.interpolate_data_from(cut_msh, n=3, exclude=["Normals", "TextureCoordinates", "Selection"])
# cut_msh.celldata.select("RGBA")
# msh.cmap("viridis_r").add_scalarbar3d("Expression level")
# show(msh, spline)
# exit()
# cut_msh.map_points_to_cells()




# # Wrap
morpher = Morpher(cut_msh, course[k], 0)
morpher.start()
show(morpher._mw, course[k])
morpher._mw.write("map.vtk")
# plt = Browser(vis)
# plt.show()
# plt.close()