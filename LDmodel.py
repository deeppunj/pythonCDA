'''
This program calculates the real and imaginary part of
the refractive indices for different metals.
I am mainly interested in Gold, Silver, and Aluminium. But you can
extend this program to include more metals.  

Input parameters:
wavelength ==> wavelength (in nm) of the exciation wave. 

materials ==> 'Au' = Gold,
              'Ag' = Sliver,
              'Al' = Aluminium,
              'Cu' = Copper,
              'Air' = Air, 

model ==> Choose between different option of, 
                        "const" = constant real refractive index,
                        "LDM" = Lorentz-Drude model
                        "cauchy" = Cauchy Model


'''


#%% importing packages   
import numpy as np


#%% make a class to the Lorentz-Drude model 

class LDM():
    def __init__(self, wavelength, material, model="LDM"):
        # get the wavelength, and the material for ex. Au, Ag or other metals
        self.wavelength = wavelength
        self.material = material
        self.model = model

        # define the constants
        c = 2.99792458E+09 # speed of light in (meters/sec)
        angFreq = 2*pi*c/self.wavelength; # angular frequency of the incident light (rad/sec)


        if self.material == 'Au':
            



