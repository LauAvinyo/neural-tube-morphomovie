from vedo import *


folder = "hoxb6"
# Load a 3D mesh of a panther from a file and set its color to blue
file = os.path.join(folder, "image-1_clean.vtk")
m = Mesh(file)
m.cmap("viridis", on="cells")

# Create a Plotter object and add the callback function to it
plt = Plotter()

# Display the mesh with the Plotter object and the docstring
plt.show(m, __doc__, axes=1).close()
