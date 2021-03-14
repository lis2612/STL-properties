# import numpy
from stl import mesh
# import sys
import argparse
# import stl
# import math


class CalcDetal():

    # Detal: mesh.Mesh

    def __init__(self, file: str):
        self.Detal = mesh.Mesh.from_file(file,
                                         calculate_normals=True,
                                         remove_duplicate_polygons=True,
                                         remove_empty_areas=True,
                                         )
        self.__PriceOfGram = 10
        self.__MaterialDensity = 1.25

    @property
    def Height(self):
        Height = self.Detal.z.max()-self.Detal.z.min()
        return Height

    @property
    def PriceOfGram(self):
        return self.__PriceOfGram

    @PriceOfGram.setter
    def PriceOfGram(self, price):
        if price >= 0:
            self.__PriceOfGram = price
        else:
            raise ValueError

    @property
    def MaterialDensity(self):
        return self.__MaterialDensity

    @MaterialDensity.setter
    def MaterialDensity(self, Density):
        if Density > 0:
            self.__MaterialDensity = Density
        else:
            raise ValueError

    @property
    def Price(self):
        vmass = self.Detal.get_mass_properties_with_density(
            self.MaterialDensity)[1]/1000
        print(vmass)
        Price = vmass*self.PriceOfGram
        return Price


if __name__ == '__main__':
    obj = CalcDetal('box.stl')
    print(obj.Height)
    print(obj.PriceOfGram)
    print(obj.MaterialDensity)
    obj.PriceOfGram = 25
    print(obj.Price)
