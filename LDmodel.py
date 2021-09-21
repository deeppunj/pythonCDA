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
              'Air' = Air, 

model ==> Choose between different option of, 
                        "const" = constant real refractive index,
                        "LDM" = Lorentz-Drude model
                        "cauchy" = Cauchy Model


'''


#%%importing packages   
import numpy as np


#%% make a class to get the Lorentz-Drude model 

class LDM():
    # LDM : Lorentz-Drude model
    def __init__(self, wavelength, material, model="LDM"):
        # get the wavelength, and the material for ex. Au, Ag or other metals
        self.wavelength = wavelength
        self.material = material
        self.model = model

        # define the constants
        c = 2.99792458e+08 # speed of light in (meters/sec)
        angFreq = 2*np.pi*c/self.wavelength; # angular frequency of the incident light (rad/sec)
        e = 1.69e-19 # mass of electron 
        hbar = 1.0545718e-34 # in m^2kg/sec


        if self.material == 'Au':
            #Plasma frequency 
            # omega_p = sqrt(n*e/m*epsilon0)
            omega_p = 9.03*e/hbar
            #oscillation strength 
            f = [0.760, 0.024, 0.010, 0.071, 0.601, 4.384]
            # Damping freq of each oscillator
            Gamma = [0.053, 0.241, 0.345, 0.870, 2.494, 2.214]
            # resonance freq of each oscillator
            omega = [0.000, 0.816, 4.481, 8.185, 9.083, 20.29]
        elif self.material == 'Ag':
            omega_p = 9.01*e/hbar
            f = [0.845, 0.065, 0.124, 0.011, 0.840, 5.646]
            Gamma = [0.048, 3.886, 0.452, 0.065, 0.916, 2.419]
            omega = [0.000, 0.816, 4.481, 8.185, 9.083, 20.29]
        elif self.material == 'Al':
            omega_p = 14.98*e/hbar
            f = [0.523, 0.227, 0.050, 0.166, 0.030]
            Gamma = [0.047, 0.333, 0.312, 1.351, 3.382]
            omega = [0.000, 0.162, 1.544, 1.808, 3.473]
        else:
            print("Give a valid material")




