from vedo.applications import Browser
from vedo import Mesh, Plotter
import os
import vedo

vedo.settings.screenshot_transparent_background = True
vis = []
# for i in range(5):
#     for r in range(11):
#         msh = Mesh(os.path.join("intermidiates", f"{i}-{i+1}-{r}.vtk")).lw(4).c("k")
#         vis.append(msh)
cmap = "RdYlBu"

# plt = Plotter()
mesh_id = 0
for a, b in ((0, 3), (3, 5)):
    for r in range(11):
        p = os.path.join("intermidiates-b", f"{a}-{b}-{r}.vtk")
        if not os.path.exists(p):
            continue
        msh = Mesh(p).lw(4).c("k")
        # pts = Points(msh.vertices)
        mesh = msh.generate_mesh(invert=True).color("k")
        mesh.smooth()
        # mesh.compute_quality()  # add a measure of triangle quality
        # mesh.map_points_to_cells()
        # mesh.cmap(cmap)

        mesh.wireframe()
        # plt += mesh
        # plt.show()
        # plt.screenshot(f"{a}-{b}-{r}.png")
        # plt -= mesh
        mesh_path = os.path.join("meshes", f"{mesh_id}.vtk")
        mesh.write(mesh_path)
        vis.append(mesh)
        mesh_id  += 1

#         except:
#             pass

plt = Browser(vis)
plt.show()
plt.close()