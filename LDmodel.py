#%% importing packages   
import numpy as np


#%% make a class to the Lorentz-Drude model 

class LDM():
    def __init__(self, wavelength, material, model="LDM"):
        # get the wavelength, and the material for ex. Au, Ag or other metals
        self.wavelength = wavelength
        self.material = material
        self.model = model



