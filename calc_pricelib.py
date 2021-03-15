from stl import mesh


class DetalCalc():
    """Calculates price 3d-print"""

# ************************** ATTRIBUTES *****************************
    __PriceOfGram = 10
    __DicOfMaterialDensity = {
        'PLA': 1.25,
        'ABS': 1.05,
        'PETG': 1.3,
        'SBS': 1.01,
        'FLEX': 1.2,
        'TPU': 1.25
    }
# ************************ END OF ATTRIBUTES ************************


# ************************** PROPERTIES *****************************

    @property
    def Height(self):
        """Model's height"""
        Height = self.Detal.z.max()-self.Detal.z.min()
        return Height

    @property
    def PriceOfGram(self):
        """Price of gram 3d-printing model"""
        return self.__PriceOfGram

    @PriceOfGram.setter
    def PriceOfGram(self, price):
        """Set price of gram 3d-printing model"""
        if price >= 0:
            self.__PriceOfGram = price
        else:
            raise ValueError

    @property
    def MaterialDensity(self):
        """Density of material"""
        return self.__MaterialDensity

    @MaterialDensity.setter
    def MaterialDensity(self, Density):
        """Set density of material"""
        if Density > 0:
            self.__MaterialDensity = Density
        else:
            raise ValueError

    @property
    def Mass(self):
        """Returnes mass of 3d-printed detal"""
        vmass = self.Detal.get_mass_properties_with_density(
            self.MaterialDensity)[1]/1000
        return vmass

    @property
    def Price(self):
        """Returnes price 3d-printing"""
        Price = self.Mass*self.PriceOfGram
        return Price
# ************************ END OF PROPERTIES ************************


# ************************ METHODS **********************************
    def PrintPrice(self):
        """Print price and mass"""
        print("********************** INVOICE ***************************")
        print("Mass       = {:.2f} g".format((self.Mass)))
        print("Price      = {:.2f} RUR" .format(self.Price))
        print("**********************************************************")

    def __init__(self, file: str, material='PLA', PrintPrice=10.0):
        """Load model from file
        file: STL model to load
        material: set material to print
                  PLA, ABS, PETG, SBS, FLEX, TPU"""
        self.Detal = mesh.Mesh.from_file(file,
                                         calculate_normals=True,
                                         remove_duplicate_polygons=True,
                                         remove_empty_areas=True,
                                         )

        if self.__DicOfMaterialDensity.get(material) is None:
            print('Material "{}" is missing'.format(material))
            print('Used default value: "PLA"')
            self.__Material = 'PLA'
        else:
            self.__Material = material
        self.__MaterialDensity = self.__DicOfMaterialDensity[self.__Material]
        self.__PriceOfGram = PrintPrice

# ************************ END OF METHODS ***************************
