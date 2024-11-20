from vedo.applications import Browser, SplinePlotter
from vedo import Mesh, Image, show, printc
import os
import sys
from vedo.applications import MorphPlotter

vis = []

cmap = "RdYlBu"

FOLDER = "hoxa7"
# CLEAN = True
# input_files = list( os.path.join(FOLDER, f)  for f in ("image-0_clean.vtk", "image-1_clean.vtk", "image-2_clean.vtk") )
input_files = list( os.path.join(FOLDER, f)  for f in ("image-0.vtk", "image-1.vtk", "image-2.vtk") )
STAGES = (5, 16, 7)


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
filepath = os.path.join(FOLDER, filename)
print(filepath)
pic = Image(filepath)

# # Check if the line has already been selected for this
# lineout = os.path.join("splines", filename.replace(".png", ".vtk"))
# if os.path.exists(lineout):
#     spline = Mesh(lineout).scale(0.01)
#     # show(pic, spline)
#     # sys.exit()
# else:
#     # Align it with each of the contour. 
#     plt = SplinePlotter(pic, closed=True)
#     plt.show(mode="image", zoom='tightest')
#     spline = plt.line.scale(0.01)
#     plt.close()

# Get the spline
plt = SplinePlotter(pic, closed=True)
plt.show(mode="image", zoom='tightest')
spline = plt.line.scale(0.01)
plt.close()

# STAGING SYSTEM
printc("Staging...", c="green")
differences = []
for k in course:
    c_spline = spline.clone()
    c_spline.align_to(course[k], rigid=True)
    distance = c_spline.distance_to(course[k], signed=False)
    differences.append((distance.mean(), k))

differences = sorted(differences)
d, k = differences[0]
# d, k = 0, 14
print(d, k)

spline.align_to(course[k])

print(f"{k} with distance {d}")
spline_mesh = spline.generate_mesh(invert=True) # TO D_2D...



# Wrap
morpher = MorphPlotter(spline.lw(10), course[k])
morpher.show()
T = morpher.warped.transform
pic_mesh = pic.bw().tomesh().apply_transform(spline.transform)
pic_mesh.apply_transform(T)

# Interpolaion 
mm_mesh_path = os.path.join("meshes", f"{k}.vtk")
mesh = Mesh(mm_mesh_path)
mesh.interpolate_data_from(pic_mesh, n=1)
mesh.pointdata.select("RGBA")
mesh.cmap("Greens")


print(morpher.warped)
show(
    mesh.cmap("Greens")
)


mesh.write(os.path.join(FOLDER, filename.replace(".png", ".vtk")))

