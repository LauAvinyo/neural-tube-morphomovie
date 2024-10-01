from vedo import Mesh, show
import os 


mesh1 = Mesh(os.path.join("splines", "image-0.vtk")).c(f"r{1}").lw(4).scale(0.9)
mesh2 = Mesh(os.path.join("splines", "image-1.vtk")).c(f"r{2}").lw(4)
mesh3 = Mesh(os.path.join("splines", "image-2.vtk")).c(f"o{3}").lw(4)
mesh4 = Mesh(os.path.join("splines", "image-3.vtk")).c(f"p{4}").lw(4)
mesh5 = Mesh(os.path.join("splines", "image-4.vtk")).c(f"g{5}").lw(4)
mesh6 = Mesh(os.path.join("splines", "image-5.vtk")).c(f"b{6}").lw(4)


mesh2.align_to(mesh1, rigid=True)
mesh3.align_to(mesh1, rigid=True)
mesh4.align_to(mesh1, rigid=True)
mesh5.align_to(mesh1, rigid=True)
mesh6.align_to(mesh1, rigid=True)


show(
    mesh1, 
    mesh2, 
    mesh3, 
    mesh4, 
    mesh5,
    mesh6
)