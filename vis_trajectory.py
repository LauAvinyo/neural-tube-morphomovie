
import json
import os
from vedo import Mesh
import numpy as np
import copy
from vedo.applications import Browser
import vedo 
print("⏳ Retrieving trajectories.")

# Load the inputs
folder_path = "meshes"
course_2d = {}
for i, filename in enumerate(sorted(
        os.listdir(folder_path), 
        key=lambda x: int(x.split(".")[0])
    )):
    filepath = os.path.join(folder_path, filename)
    if os.path.isfile(filepath):
        m = Mesh(filepath)
        course_2d[i] = m

print(course_2d.keys())
file_path = 'trajectories.json'
with open(file_path, 'r') as file:
    trajectories = json.load(file)

# for tr in trajectories:
#     print(len(tr))

trajectory = trajectories[np.random.randint(0, 1000)]
# trajectory = trajectories


frames = []
for tr, t in trajectory:
    t = int(t)
    if t in course_2d:
        m = course_2d[t].clone()
        m.celldata["values"] = np.zeros(len(m.cells))
        m.celldata["values"][int(tr)]= 1
        m.cmap("Reds", "values", on="cells")
        frames.append(m)

plt = Browser(frames)
plt.show().close()