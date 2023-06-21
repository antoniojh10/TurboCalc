import numpy as np

g = 9.81

class Volute():
    def __init__(self, pump):
        '''Methode Stepanoff'''
        Kcm = 1.8 / (3.65*pump.nq)**(1/3)
        c_v = Kcm * (2 * g * pump.H_opt)**0.5
        self.angles = np.arange(0, 360, 10)

        self.R = 0.5 * ((self.angles*pump.Q_opt) / (90*np.pi*c_v))**0.5
        
        