import numpy as np
import pandas as pd

class NewCSV():
    def __init__(self, pump, volute):
        self.savePumpCSV(pump)
        self.saveVoluteCSV(volute)
        
    def savePumpCSV(self, pump):
        data_pump = {
            'property': ['n', 'H_opt', 'Q_opt', 'rho', 'nq', 'eta', 'eta_hy', 'P', 'dw_min', 'dw', 'Psi_opt', 'D2', 'D1', 'c1m', 'u1', 'beta1', 'b2', 'c2m', 'u2', 'c2u', 'beta2', 'e', 'Ze'],
            'value': [pump.n, pump.H_opt, pump.Q_opt, pump.rho, pump.nq, pump.eta*100, pump.eta_hy*100, pump.P, pump.dw_min*1000, pump.dw, pump.psi_opt, pump.D2, pump.D1, pump.c1m, pump.u1, pump.beta1*180/np.pi, pump.b2, pump.c2m, pump.u2, pump.c2u, pump.beta2*180/np.pi, pump.e, pump.Ze],
            'unit': ['rpm', 'm', 'm3/s', 'kg/s', '', '%', '%', 'W', 'mm', 'mm', '', 'mm', 'mm', 'm/s', 'm/s', '°', 'mm', 'm/s', 'm/s', 'm/s', '°', 'mm', 'mm']
        }
        
        df_pump = pd.DataFrame(data_pump, columns=['property', 'value', 'unit'])
        df_pump.to_csv('output.csv')
        
    def saveVoluteCSV(self, volute):
        data_volute = {
            'angle': volute.angles,
            'R': volute.R
        }
        
        df_volute = pd.DataFrame(data_volute, columns=['angle', 'R'])
        df_volute.to_csv('output_volute.csv')
        
        
        