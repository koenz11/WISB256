from scipy.integrate import odeint
from scipy.linalg import eig
from numpy import arange
from numpy import array

class Lorenz:
    def __init__(self, startValues, sigma = 10, rho = 28, betta = float(8)/float(3)):
        self.startValues = startValues
        self.sigma = sigma
        self.rho = rho
        self.betta = betta
    
    def LorenzFunc(self, last, t):
        [x, y, z] = last
        return[self.sigma*(y - x), x*(self.rho - z) -y, x*y - self.betta*z]
    
        
    def solve(self, T, dt):
        tijdstappen = arange(0, T, dt)
        
        vector = odeint(self.LorenzFunc, self.startValues, tijdstappen) 
        return vector
        
    def df(self, u):
        [x, y, z] = u
        #jacobian = array([[self.sigma, self.sigma, 0], [self.rho-z, -1, -x], [y, x, -self.betta]])
        jacobian = array([[self.sigma, self.rho-z, y], [self.sigma, -1, x], [0, -x, -self.betta]])
        #print(jacobian)
        return jacobian
        

    def isStable(self, u):
        eigenvalues = eig(self.df(u))
        
        #print(eigenvalues)
        
        for value in eigenvalues[0]:
            if value > 0:
                return False
        
        return True
        