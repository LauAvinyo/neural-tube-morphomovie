import vedo
from matplotlib import pyplot as plt
import numpy as np 
import os 
import json
from vedo.applications import Browser
from vedo import Video
CLEAN = False


folder = "hoxa7"
# input_files = list( os.path.join(folder, f)  for f in ("image-0.vtk", "image-1.vtk", "image-2.vtk") )
STAGES = (5, 7, 16, 13)


CLEAN = True
input_files = list( os.path.join(folder, f)  for f in ("image-0_clean.vtk",  "image-2_clean.vtk", "image-1_clean.vtk", "image-3_clean.vtk") )

cam = dict(
    pos=(2.60475, 2.36445, 17.9360),
    focal_point=(2.60475, 2.36445, 3.79362e-9),
    viewup=(0, 1.00000, 0),
    roll=0,
    distance=17.9360,
    clipping_range=(16.8002, 19.4089),
)


def normalize(v):
    return (v - v.min()) / (v.max() - v.min())

# Read the trajectories
with open("trajectories.json", "r") as f:
    trajectories = json.load(f)

# Load the data
data = []
for i, f in enumerate(input_files):
    print(f)
    mesh = vedo.Mesh(f)
    print(mesh)
    if not CLEAN:
        # Mix Max normalitzation of the data
        values = mesh.pointdata["RGBA"]
        values = normalize(values)
        values = 1 - values
        # values[values < values.mean()] = 0
        mesh.pointdata["expression"] = values
        mesh.smooth_data()
        mesh.map_points_to_cells()
    else:
        values = mesh.celldata["clean_expression"]
        values = normalize(values)
        # # if i == 0 or i == 2:
        # #     values = 1 - values
        mesh.celldata["expression"] = values
        mesh.map_cells_to_points()
        mesh.smooth_data(niter=100)
        mesh.map_points_to_cells()
    data.append((STAGES[i], mesh))
    mesh.cmap("viridis")
    # print(mesh)

data = sorted(data)
frames = list(v for _, v in data)
# plt = Browser(frames)
# plt.show().close()
# exit()
min_time = min(STAGES)
max_time = max(STAGES)

morphomovie_timepoints = np.arange(min_time, max_time + 1)
number_timepoints = len(morphomovie_timepoints)

folder_path = "meshes"
course_2d = {}
for i in morphomovie_timepoints:
    filepath = os.path.join(folder_path, f"{i}.vtk")
    if os.path.isfile(filepath):
        m = vedo.Mesh(filepath)
        course_2d[int(i)] = m

reconstruction = {
    int(t): {str(n): [] for n in range(len(course_2d[t].cells))}
    for t in morphomovie_timepoints
}

for trajectory in trajectories:
    trajectory_dict = dict((int(t), n) for n, t in trajectory)
    x, y = [], []
    for tr, t in trajectory:
        t = int(t)
        if t < min_time or t > max_time: continue
        for ct, d in data:
            # print(ct)
            if ct == t:
                x.append(int(t))
                y.append(d.celldata["expression"][int(tr)])
        
    points = np.column_stack((x, y))
    points = np.unique(points.round(8), axis=0)
    spline = vedo.Spline(points, smooth=1, res=number_timepoints + 1)
    i_points = spline.vertices
    x_interpolated = i_points[:, 0]
    y_interpolated = i_points[:, 1]
    y_interpolated[y_interpolated < 0] = 0

    for timepoint in morphomovie_timepoints:
        timepoint = int(timepoint)
        # Get the closest value in the curve
        index = np.abs(x_interpolated - timepoint).argmin()
        value = float(y_interpolated[index])

        # Get the triangle
        # timepoint = mesh_bmap_tp.get(timepoint, timepoint)
        triangle = str(int(trajectory_dict[timepoint]))
        # print(reconstruction[timepoint])

        reconstruction[timepoint][triangle].append(value)
    # break
interpolation = {}
for t in reconstruction:
    interpolation[t] = []
    for tr in sorted(reconstruction[t], key=lambda x: int(x)): 
        m = np.mean(reconstruction[t][tr])
        interpolation[t].append(m)


frames = []
for t in interpolation:
    print(t)
    mesh = course_2d[int(t)].cmap("viridis")
    mesh.celldata["expression"] = interpolation[t]
    mesh.smooth()
    frames.append(mesh)

# plt = Browser(frames)
# plt.show()

# plt = vedo.Plotter()
# plt.add(frames[-1])
# plt.show()


plt = vedo.Plotter()

# # I Use this code to get the camera
# plt.add(frames[-1])
# plt.show()


video = Video("vedo_video.mp4", duration=3) # or gif
# Any rendering loop goes here, e.g.:
for frame in frames:
    frame.name = "in"
    plt.add(frame)
    plt.show(camera=cam)  # render the scene
    video.add_frame()
    plt.remove("in")




# video.action()
video.close() 

plt.interactive().close()