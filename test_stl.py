import numpy
from stl import mesh
from mpl_toolkits import mplot3d
from matplotlib import pyplot
import sys

def calculate(f):
    # Create a new plot
    figure = pyplot.figure()
    axes= mplot3d.Axes3D(figure)

    # Load the STL files and add the vectors to the plot
    your_mesh = mesh.Mesh.from_file(f)
    axes.add_collection3d(mplot3d.art3d.Poly3DCollection(your_mesh.vectors))

    # Auto scale to the mesh size
    #scale = your_mesh.points.flatten()
    #axes.auto_scale_xyz(scale, scale, scale)

    # Show the plot to the screen
    #pyplot.show()

    volume, cog, inertia = your_mesh.get_mass_properties()
    volume=volume/1000
    print("Volume                                  = {:.2f} cm^3".format(volume))
    mass=round(volume*1.25)
    print("Mass                                    = {:.2f} g".format(mass))
    price=mass*2000/1000*5
    print("Price                                   ={:.2f} RUR" .format(price))
    #help('FORMATTING')

if __name__ == "__main__":
    if len (sys.argv) > 1:
        #print(type(sys.argv[1]))
        calculate(sys.argv[1])
    else:
        print ("В аргументах не указано имя файла. Формат использования: test_stl.py file.stl")
