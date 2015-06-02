from scipy.integrate import odeint
from numpy import arange
import random

class Lorenz:
    def __init__(self, startValues, sigma = 10, rho = 28, betta = 8/3):
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