from centrifugalPump import CentrifugalPump

n = float(input('Select a speed n in [rpm]: '))
H_opt = float(input('Select a H_opt in [m]: '))
Q_opt = float(input('Select a Q_opt in [m3/s]: '))
rho = float(input('Select a density rho in [kg/m3] for the fluid: '))

pump = CentrifugalPump(Q_opt, H_opt, n, rho)