
import json
import os
from vedo import Mesh
import numpy as np
import copy

#TODO FIX ALL OF THESE!
# Load the inputs
folder_path = "meshes"
course_2d = []
for filename in sorted(
        os.listdir(folder_path), 
        key=lambda x: int(x.split(".")[0])
    ):
    filepath = os.path.join(folder_path, filename)
    if os.path.isfile(filepath):
        m = Mesh(filepath).wireframe()
        course_2d.append(m)

file_path = 'interpolation_map.json'
with open(file_path, 'r') as file:
    imap = json.load(file)

with open("bmap.json", 'r') as file:
    bmap = json.load(file)
print("Files Loaded!")


# NOTE: This is needed to compute the backwards map
# bmap = {}
# for tp in imap:    
#     bmap[int(tp)] = {}

#     set_u = set()
#     ti = tp # str(int(tp))
#     for v in imap[ti]:
#         for u in imap[ti][v]:
#             set_u.add(u)

#     for u in set_u:
#         bmap[int(tp)][u] = {}
#         for v in imap[ti]:
#             if u in imap[ti][v]:
#                 bmap[int(tp)][u][v] = imap[ti][v][u]

# with open("bmap.json", 'w') as file:    
#     json.dump(bmap, file, indent=4) 

# for tp in bmap:
#     print(len(bmap[tp]), len(course_2d[int(tp)].cells))
# print("Backwards map done!")

timepoints = sorted(list(int(i) for i in bmap.keys()), reverse=True)
# print(timepoints)

print("⏳ Retrieving trajectories.")


# The backwards step. No need to recompute it. 
# If needed just uncomment this!
# # Trajectiories through time
# full_trajectories = {}
# full_triangles = {}

# for t in bmap:
#     full_triangles[int(t)] = set()


# for i, t in enumerate(timepoints):
#     full_trajectories[t] = {}

#     for root in bmap[str(t)]:
#         node = root
#         full_triangles[t].add(root)
#         trajectory = []
#         for j in range(i, len(timepoints) - 1):
#             tp = timepoints[j]
#             trajectory.append((node, tp))
#             node = max(bmap[str(tp)][node], key=bmap[str(tp)][node].get)
#             full_triangles[tp].add(node)

#         full_trajectories[t][root] = trajectory

# full_trajectories.pop(t)

# trajectories = full_trajectories

# trajectories_collection = []
# for t in trajectories:
#     for k in trajectories[t]:
#         trj = trajectories[t][k]
#         trajectories_collection.append(trj)

# print("⏳ Pruning trajectories.")
# sorted_times = sorted(timepoints)
# unique_trajectories = []
# for t in range(1, len(timepoints) - 1):
#     t1 = sorted_times[t]
#     t2 = sorted_times[t + 1]

#     if t1 % 100 == 0:
#         print(t1, t2)

#     for trj in trajectories[t1].values():
#         found = False
#         for can in trajectories[t2].values():
#             if set(trj) <= set(can):
#                 found = True
#                 break

#         if not found:
#             unique_trajectories.append(trj)

# for trj in trajectories[t2].values():
#     unique_trajectories.append(trj)

# unique_trajectories = set(tuple(i) for i in unique_trajectories)
# with open("trajectories-tmp.json", 'w') as file:    
#     json.dump(list(unique_trajectories), file, indent=4) 
with open("trajectories-tmp.json", 'r') as file:    
    unique_trajectories = json.load(file) 


# for tr in unique_trajectories:
#     timepoints = list(i for _, i in tr)
#     if 19 in timepoints:
#         print(tr)

# exit()
# print(len(unique_trajectories))

max_length = len(max(unique_trajectories, key=lambda x: len(x)))
print(f"The max length is {max_length}")


print("⏳ Complete the trajectories" )
forward_times = np.array(sorted(list(int(i) for i in imap.keys())))
full_trajectories = set()
non_finished = 0
for i, tr in enumerate(unique_trajectories):

    # Back to tuple after json load! 
    tr = tuple(tuple(i) for i in tr)
    if len(tr) == 1:
        continue

    if len(tr) == 18:
        full_trajectories.add(tuple(tr))
        continue
    else:
        non_finished += 1
    
    # Get the trajectory
    tr = sorted(tr, key=lambda x: x[1])
    last_timepoint = tr[-1][1]
    forward = forward_times[forward_times >last_timepoint]

    n, t = tr[-1]
    p = t

    new_trajectory = copy.copy(tr)
    for t in forward:
        t = str(t)
        if imap[t].get(n, False):
            n = max(imap[t][n], key=imap[t][n].get)
            p = t
        else:
            print("WE here! ")
        new_trajectory.append((n, t))
    if len(new_trajectory) != 18: 
        print("Something not working", len(new_trajectory))
        break
    else:
        full_trajectories.add(tuple(tuple(i) for i in new_trajectory))
print(non_finished)
full_trajectories = sorted(list(full_trajectories))

# Specify the file path
file_path = 'trajectories.json'
with open(file_path, 'w') as file:
    json.dump(full_trajectories, file, indent=4)  # `indent=4` makes it more readable



print("We got to the end!")