import vedo 
import os
import numpy as np
from vedo import Mesh, Points, show, Arrows, progressbar, CellCenters
from vedo.applications import Browser
import json
folder_path = 'meshes'

# Iterate through all files in the folder
course_1d = []
course_2d = []
for filename in sorted(
        os.listdir(folder_path), 
        key=lambda x: int(x.split(".")[0])
    ):
    filepath = os.path.join(folder_path, filename)
    if os.path.isfile(filepath):
        print(filename)
        m = Mesh(filepath).wireframe()
        b = m.boundaries()
        course_1d.append(b)
        course_2d.append(m)


def find_closest_point(points_array, point):
    distances = np.linalg.norm(points_array - point, axis=1)
    closest_index = np.argmin(distances)
    return closest_index

fmap = {}
for c_id in range(len(course_1d) - 1):
    current_boundary = course_1d[c_id]
    next_boundary = course_1d[c_id + 1]

    points = []
    next_clone = next_boundary.clone().subsample(0.01)
    for p in next_clone.vertices:
        cp = current_boundary.closest_point(p)
        points.append((cp, p))
    points = np.array(points)
    source_points = Points(points[:, 0])
    target_points = Points(points[:, 1])
    current_boundary.warp(source_points, target_points)
    transform = current_boundary.transform
    
    # Triangle interpolation
    current_mesh = course_2d[c_id].apply_transform(transform)
    next_mesh = course_2d[c_id + 1]

    k = f"{c_id + 1}"
    fmap[k] = {}
    
    
    c0 = CellCenters(current_mesh)
    c1 = CellCenters(next_mesh)
    n0 = c0.npoints
    for i in progressbar(n0, title=f"Loop through points in limb {c_id}"):

        # Set the scalars of limb0 to 0 except at point i
        arr0 = np.zeros(n0).astype(float)
        arr0[i] = 1.0
        c0.pointdata["scalar"] = arr0

        c1_clone = c1.clone().interpolate_data_from(c0, n=3)
        arr1 = c1_clone.pointdata["scalar"]

        # Find the indices where the values are not zero
        ids = np.where(arr1 != 0)[0]

        if len(ids) == 0:
            # Pick the closest point.
            ids = [find_closest_point(c1.vertices, c0.vertices[i])]


        # break
        # Store it on the fmap
        fmap[k][i] = dict([(int(k), float(arr1[k])) for k in ids])
        # show(
        #     c0.cmap("Reds", "scalar"), 
        #     c1_clone.cmap("Blues", "scalar").z(1)
        # )

file_path = 'interpolation_map.json'
with open(file_path, 'w') as file:
    json.dump(fmap, file, indent=4) 


# plt = Browser(course)
# plt.show()current_mesh

# plt.close()


    # show(
    #         next_mesh, 
    #         s, 
    #         t,
    #         Arrows(points[:, 0], points[:, 1]),
    #         c
    #     ).close()