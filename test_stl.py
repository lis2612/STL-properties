import numpy
from stl import mesh
# from mpl_toolkits import mplot3d
# from matplotlib import pyplot
import sys
import argparse
import stl
import math


def createParser():
    parser = argparse.ArgumentParser()
    # Добавляем аргументы
    parser.add_argument('file', nargs='?', help='Filename STL model')
    parser.add_argument('-p', '--price',   nargs='?', type=float, default=10,
                        help='Price of gram 3d-printing model. Default=10')
    parser.add_argument('-d', '--density', nargs='?', type=float, default=1.25,
                        help='Density of material. Default=1.25')
    parser.add_argument('-i', '--indensity', nargs='?', type=float, default=0.2,
                        help='Density of infill pattern. Default=0.2')
    parser.add_argument('-t', '--thicken', nargs='?', type=float, default=1,
                        help='Shell thicken. Default=1')
    return parser

def getObjHeight(obj):
    return obj.z.max()-obj.z.min()

# def toDecart(r,theta,phi):
#     x=round(r*math.sin(theta)*math.cos(phi),5)
#     y=round(r*math.sin(theta)*math.sin(phi),5)
#     z=round(r*math.cos(theta),5)
#     # print("To Decart:",x,y,z)
#     return x,y,z

# def toSphere(x,y,z):
#     r=math.sqrt(x*x+y*y+z*z)
#     theta=math.acos(z/r)
#     phi=math.atan(y/x)
#     # print(x,y,z)
#     # print("To Sphere:",r,theta,phi)
#     # toDecart(r,theta,phi)
#     return r,theta,phi
    

    # Функция расчета стоимости печати изделия
    # f - STL файл модели
    # gramm_price - стоимость печати за грамм готового изделия
    # density - плотность материала
    # infill_density - плотность рисунка заполнения
    # shell_thicken - толщина стенок
def calculate(f, gramm_price, density,infill_density,shell_thicken):
    
    # Load the STL file
    your_mesh = mesh.Mesh.from_file(f, remove_duplicate_polygons=True, remove_empty_areas=True, calculate_normals=True)
    # Get model characteristics
    volume, vmass, cog, inertia = your_mesh.get_mass_properties_with_density(density)
    # print("Volume     = {:.2f} cm^3".format(volume/1000))
    # print("Mass       = {:.2f} g".format((vmass/1000),1))
    # print("Price      = {:.2f} RUR" .format(vmass/1000*gramm_price))
    
    #Calculate infill volume   
    kscale=1-2*shell_thicken/getObjHeight(your_mesh)
    your_mesh.data['vectors']*=kscale
    infill_volume, infill_vmass, infill_cog, infill_inertia = your_mesh.get_mass_properties_with_density(density*infill_density)
    # print("Volume     = {:.2f} cm^3".format(infill_volume/1000))
    # print("Mass       = {:.2f} g".format((infill_vmass/1000)))
    # print("Price      = {:.2f} RUR" .format(infill_vmass/1000*gramm_price))
    

    # Calculate mass and price of detal
    shell_mass=(volume-infill_volume)*density
    detal_mass=infill_vmass+shell_mass
    detal_price=detal_mass/1000*gramm_price

    print("********************** INVOICE ***************************")
    print("Mass       = {:.2f} g".format((detal_mass/1000)))
    print("Price      = {:.2f} RUR" .format(detal_price))
    print("**********************************************************")

    # your_mesh.save('new.stl')
                


if __name__ == "__main__":
    parser = createParser()
    namespace = parser.parse_args()
   
    if namespace.file == None:
        parser.print_help()
        
    if namespace.file:
        calculate(namespace.file, namespace.price, namespace.density,namespace.indensity,namespace.thicken)
        
