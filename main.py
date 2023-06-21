from centrifugalPump import CentrifugalPump
from volute import Volute
from printCSV import NewCSV

# --------- INPUT SECTION ----------
n = float(input('Select a speed n in [rpm]: '))
H_opt = float(input('Select a H_opt in [m]: '))
Q_opt = float(input('Select a Q_opt in [m3/s]: '))
rho = float(input('Select a density rho in [kg/m3] for the fluid: '))

# --------- TEST VALUES ----------
#n = 20000
#H_opt = 1200
#Q_opt = 0.063
#rho = 72

pump = CentrifugalPump(Q_opt, H_opt, n, rho)
volute = Volute(pump)
NewCSV(pump, volute)