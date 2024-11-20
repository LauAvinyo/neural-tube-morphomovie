import os


# TEST GENE
input_files = (
    os.path.join("test_gene", "image-2.vtk"), 
    os.path.join("test_gene", "image-3.vtk"), 
    os.path.join("test_gene", "image-4.vtk"), 
    os.path.join("test_gene", "image-5.vtk"), 
)
STAGES = (9, 11, 14, 19)
input_files = (
    os.path.join("test_gene", "image-2_clean.vtk"), 
    # os.path.join("test_gene", "image-3_clean.vtk"), 
    os.path.join("test_gene", "image-4_clean.vtk"), 
    os.path.join("test_gene", "image-5_clean.vtk"), 
)
CLEAN = True
STAGES = (9, 14, 19)


# # Ralhd2
# folder = "raldh2"
# # input_files = (
# #     os.path.join(folder, "image-0.vtk"), 
# #     os.path.join(folder, "image-1.vtk"), 
# #     os.path.join(folder, "image-2.vtk"), 
# #     os.path.join(folder, "image-3.vtk")
# # )
# # STAGES = (13, 13, 9, 19)

# CLEAN = True
# input_files = (
#     os.path.join(folder, "image-0_clean.vtk"), 
#     os.path.join(folder, "image-1_clean.vtk"), 
#     # os.path.join(folder, "image-2_clean.vtk"), 
#     os.path.join(folder, "image-3_clean.vtk")
# )
# STAGES = (17,  12, 19)

# cam = dict(
#     pos=(2.55349, 2.37809, 19.0059),
#     focal_point=(2.55349, 2.37809, 1.76256e-7),
#     viewup=(0, 1.00000, 0),
#     roll=0,
#     distance=19.0059,
#     clipping_range=(17.8024, 20.5667),
# )

# # Hoxb11
# folder = "hoxb11"
# input_files = (
#     os.path.join(folder, "image-0.vtk"), 
#     # os.path.join(folder, "image.vtk"), 
#     os.path.join(folder, "image-1.vtk"), 
#     # os.path.join(folder, "image-3.vtk")
# )
# STAGES = (19, 11)

# folder = "TGF"
# input_files = (
#     os.path.join(folder, "image-0.vtk"), 
#     os.path.join(folder, "image-1.vtk"), 
#     os.path.join(folder, "image-2.vtk"), 
#     # os.path.join(folder, "image-3.vtk")
# )
# STAGES = (17, 19, 14)


# folder = "hoxb6"
# input_files = (
#     os.path.join(folder, "image-0.vtk"), 
#     os.path.join(folder, "image-1.vtk"), 
#     os.path.join(folder, "image-2.vtk"), 
#     # os.path.join(folder, "image-3.vtk")
# )
# STAGES = (3, 7, 13)

folder = "hoxb6"
input_files = (
    os.path.join(folder, "image-0_clean.vtk"), 
    os.path.join(folder, "image-1_clean.vtk"), 
    os.path.join(folder, "image-2_clean.vtk"), 
    # os.path.join(folder, "image-3.vtk")
)
CLEAN = True
STAGES = (3, 7, 13)

cam = dict(
    pos=(2.65500, 2.33179, 16.9195),
    focal_point=(2.65500, 2.33179, -2.58084e-7),
    viewup=(0, 1.00000, 0),
    roll=0,
    distance=16.9195,
    clipping_range=(15.8481, 18.3089),
)




# TEST GENE
input_files = (
    os.path.join("test_gene", "image-2.vtk"), 
    os.path.join("test_gene", "image-3.vtk"), 
    os.path.join("test_gene", "image-4.vtk"), 
    os.path.join("test_gene", "image-5.vtk"), 
)
STAGES = (9, 11, 14, 19)
input_files = (
    os.path.join("test_gene", "image-2_clean.vtk"), 
    # os.path.join("test_gene", "image-3_clean.vtk"), 
    os.path.join("test_gene", "image-4_clean.vtk"), 
    os.path.join("test_gene", "image-5_clean.vtk"), 
)
CLEAN = True
STAGES = (9, 14, 19)

cam = dict(
    pos=(2.55349, 2.37809, 19.0059),
    focal_point=(2.55349, 2.37809, 1.76256e-7),
    viewup=(0, 1.00000, 0),
    roll=0,
    distance=19.0059,
    clipping_range=(17.8024, 20.5667),
)


# # Ralhd2
# folder = "raldh2"
# # input_files = (
# #     os.path.join(folder, "image-0.vtk"), 
# #     os.path.join(folder, "image-1.vtk"), 
# #     os.path.join(folder, "image-2.vtk"), 
# #     os.path.join(folder, "image-3.vtk")
# # )
# # STAGES = (13, 13, 9, 19)

# CLEAN = True
# input_files = (
#     os.path.join(folder, "image-0_clean.vtk"), 
#     os.path.join(folder, "image-1_clean.vtk"), 
#     # os.path.join(folder, "image-2_clean.vtk"), 
#     os.path.join(folder, "image-3_clean.vtk")
# )
# STAGES = (17,  12, 19)

# cam = dict(
#     pos=(2.55349, 2.37809, 19.0059),
#     focal_point=(2.55349, 2.37809, 1.76256e-7),
#     viewup=(0, 1.00000, 0),
#     roll=0,
#     distance=19.0059,
#     clipping_range=(17.8024, 20.5667),
# )

# # Hoxb11
# folder = "hoxb11"
# input_files = (
#     os.path.join(folder, "image-0.vtk"), 
#     # os.path.join(folder, "image.vtk"), 
#     os.path.join(folder, "image-1.vtk"), 
#     # os.path.join(folder, "image-3.vtk")
# )
# STAGES = (19, 11)

# folder = "TGF"
# input_files = (
#     os.path.join(folder, "image-0.vtk"), 
#     os.path.join(folder, "image-1.vtk"), 
#     os.path.join(folder, "image-2.vtk"), 
#     # os.path.join(folder, "image-3.vtk")
# )
# STAGES = (17, 19, 14)


# folder = "hoxb6"
# input_files = (
#     os.path.join(folder, "image-0.vtk"), 
#     os.path.join(folder, "image-1.vtk"), 
#     os.path.join(folder, "image-2.vtk"), 
#     # os.path.join(folder, "image-3.vtk")
# )
# STAGES = (3, 7, 13)

# folder = "hoxb6"
# input_files = (
#     os.path.join(folder, "image-0_clean.vtk"), 
#     os.path.join(folder, "image-1_clean.vtk"), 
#     os.path.join(folder, "image-2_clean.vtk"), 
#     # os.path.join(folder, "image-3.vtk")
# )
# CLEAN = True
# STAGES = (3, 7, 13)

# cam = dict(
#     pos=(2.65500, 2.33179, 16.9195),
#     focal_point=(2.65500, 2.33179, -2.58084e-7),
#     viewup=(0, 1.00000, 0),
#     roll=0,
#     distance=16.9195,
#     clipping_range=(15.8481, 18.3089),
# )