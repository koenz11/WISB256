import math

class Vector:
    data = []
    def __init__(self, n, elements = None):
        if elements == None:
            self.data = [0]*n
        elif isinstance(elements, list):
            self.data = elements
        else:
            self.data = [elements]*n
    
    def __str__(self):
        returnString = ""
        for x in range(len(self.data)):
            returnString += str(self.data[x])
            if not x == len(self.data) -1:
             returnString += "\n"
        return returnString
    
    
    def lincom(self, other, alpha, beta):
        data = self.data.copy()
        for x in range(len(data)):
            data[x] = self.data[x]*alpha
            if not other == None:
                data[x] += other.data[x]*beta
        return Vector(len(data), data)
        
    
    def scalar(self, alpha):
        return self.lincom(None, alpha, 0)
    
    def inner(self, other):
        value = 0
        for x in range(len(self.data)):
            if not other == None:
                value += self.data[x] * other.data[x]
            else:
                value += self.data[x]*self.data[x]
                
        
        return value
    
    def norm(self):
        return math.sqrt(self.inner(None))
    
def GrammSchmidt(vectorList):
    u = [vectorList[0].scalar(1/vectorList[0].norm())]
    for x in range(1, len(vectorList)):
        projVector = Vector(len(u[0].data), 0)
        for k in range(0, len(u)):
            projVector = projVector.lincom(proj(u[k], vectorList[x]), 1, 1)
        newVector = vectorList[x].lincom(projVector, 1, -1)
        u.append(newVector.scalar(1/newVector.norm()))
    return u


def proj(vector1, vector2):
    above = vector2.inner(vector1)
    below = vector1.inner(vector1)
    return vector1.scalar(above/below)

