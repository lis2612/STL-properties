import numpy
from stl import mesh
from mpl_toolkits import mplot3d
from matplotlib import pyplot
import sys
import argparse

def createParser ():
    parser = argparse.ArgumentParser()
    #Добавляем аргументы
    parser.add_argument ('-f','--file', nargs='?',help='Filename STL model')
    parser.add_argument('-p','--price',nargs='?',default=10,help='Price of gram 3d-printing model')
    return parser

def calculate(f,gramm_price):
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
    price=mass*gramm_price
    print("Price                                   ={:.2f} RUR" .format(price))
    #help('FORMATTING')

if __name__ == "__main__":
    parser = createParser()
    namespace = parser.parse_args()
    print (namespace)

    if namespace.file==None:
        parser.print_help()
    if namespace.file:
        calculate(namespace.file,float(namespace.price))
    
