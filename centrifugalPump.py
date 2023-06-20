import numpy as np

g = 9.81

class CentrifugalPump():
    def __init__(self, Q, H, n, rho):
        self.H_opt = H
        self.Q_opt = Q
        self.n = n
        self.rho = rho
        
        self.calc_nq()
        if self.validateNq():
            print("nq should be between 7 and 30 for centrifugal pumps")
        else:
            self.Efficiency()
            self.HydraulicEfficiency()
            self.Power()
            self.calc_minDw()
            
            # SELECT DW
            self.dw = 0
            while self.dw < self.dw_min*1000:
                print('Select a dw greater than', round(self.dw_min*1000, 2))
                self.dw = float(input('in mm: '))
                
            print('dw:', round(self.dw, 2), 'mm')
            
            self.PsiOpt()
            self.calc_D2()
            
            # SELECT NUMBER OF BLADES
            
            self.calc_D1()
            self.calc_Inlet()
            
            self.calc_b2()
            self.calc_Outlet()
            
            self.bladeThickness()
            self.calc_Ze_distance()
        
    def calc_nq(self):
        ''''Gulich 3.4.15'''
        self.nq = self.n * self.Q_opt**0.5 / self.H_opt**0.75
        print('nq: ', round(self.nq, 2))
        
    def validateNq(self):
        return self.nq > 30 or self.nq < 7
        
    def Efficiency(self):
        ''''Gulich 3.9.1'''
        Qref = 1
        if self.Q_opt > 1.0:
            a = 0.5
        else:
            a = 1.0
        m = 0.1*a*(Qref/self.Q_opt)**0.15*(45.0/self.nq)**0.06
        self.eta = 1-0.095*(Qref/self.Q_opt)**m-0.3*(0.35-np.log10(self.nq/23.0))**2*(Qref/self.Q_opt)**0.05
        print('eta:', round(self.eta*100, 2), '%')
        
    def HydraulicEfficiency(self):
        ''''Gulich 3.9.6'''
        Qref = 1
        if self.Q_opt > 1.0:
            a = 0.5
        else:
            a = 1
        m = 0.08*a*(Qref/self.Q_opt)**0.15*(45/self.nq)**0.06
        self.eta_hy = 1-0.055*(Qref/self.Q_opt)**m-0.2*(0.26-np.log10(self.nq/25))**2*(Qref/self.Q_opt)**0.1
        print('eta_h:', round(self.eta_hy*100, 2), '%')
        
    def Power(self):
        self.P = self.Q_opt * self.H_opt * self.rho * g / self.eta
        print('P:', round(self.P, 2), 'W')
        
    def calc_minDw(self, Tau=15000000):
        ''''Gulich 7.1.2'''
        self.dw_min = 3.65*(self.P/(self.n*Tau))**(1/3)
        print('dw_min:', round(self.dw_min*1000, 2), 'mm')
        
    def PsiOpt(self):
        '''Gulich 15.1.9'''
        nq_ref = 100
        self.psi_opt = 1.21*np.e**(-0.77*self.nq/nq_ref)
        print('psi_opt:', round(self.psi_opt, 4))
        
    def Psi0(self):
        '''Gulich 15.1.15'''
        nq_ref = 100
        self.psi_0 = 1.25*np.e**(-0.3*self.nq/nq_ref)
        print('psi_0:', round(self.psi_0, 4))
          
    def calc_D2(self):
        '''Gulich 15.1.10. [mm]'''
        self.D2 = 84.6 / self.n * np.sqrt(self.H_opt / self.psi_opt) * 1000
        print('D2:', round(self.D2, 2), 'mm')
        
    def calc_D1(self):
        lambdaC=1.15
        lambdaW=0.2
        dw_meters = self.dw / 1000
        self.D1 = np.sqrt(dw_meters**2 + 10.6*(self.Q_opt/self.n)**(2/3)*((lambdaC+lambdaW)/lambdaW)**(1/3))*1000
        print('D1:', round(self.D1, 2), 'mm')
        
    def calc_Inlet(self):
        dn = self.dw/1000
        d1 = self.D1/1000

        self.c1m = self.Q_opt / ((np.pi/4)*(d1**2 - dn**2))
        print('c1m:', round(self.c1m, 2), 'm/s')

        self.u1 = np.pi * self.n * d1 / 60
        print('u1:', round(self.u1, 2), 'm/s')

        self.beta1 = np.arctan(self.c1m / self.u1)
        print('beta1:', round((self.beta1)*180/np.pi, 2), '°')
        
    def calc_b2(self):
        '''Gulich 7.1'''
        nq_ref = 100
        b2_etoile = 0.017+0.262*(self.nq/nq_ref) - 0.08*(self.nq/nq_ref)**2 + 0.0093*(self.nq/nq_ref)**3
        self.b2 = self.D2*b2_etoile
        print('b*:', round(b2_etoile, 3), '')
        print('b2:', round(self.b2, 2), 'mm')
        
    def calc_Outlet(self):
        dn = self.dw/1000
        d2 = self.D2/1000

        self.c2m = self.Q_opt / (np.pi*d2*self.b2)
        print('c2m:', round(self.c2m, 2), 'm/s')

        self.u2 = np.pi * self.n * d2 / 60
        print('u2:', round(self.u2, 2), 'm/s')
        
        self.c2u = g * self.H_opt / (self.eta_hy * self.u2)
        print('c2u:', round(self.c2u, 2), 'm/s')

        # SELECT BETA 2
        beta2 = 0
        while beta2 < 20 or beta2 > 27:
            beta2 = float(input('Select an angle Beta 2 between 20 and 27 degrees: '))
        self.beta2 = beta2*np.pi/180
        print('beta2:', round(self.beta2*180/np.pi, 2), '°')
        
    def bladeThickness(self):
        if self.H_opt > 600:
            self.e = 0.022*self.D2
        else:
            self.e = 0.019*self.D2
        print('e:', round(self.e, 2), 'mm')
        
    def calc_Ze_distance(self):
        nq_ref = 74
        self.Ze = (self.D2 - self.D1)*(self.nq/nq_ref)**1.07
        print('Ze:', round(self.Ze, 2), 'mm')