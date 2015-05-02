import random
import sys
import math

def drop_needle(L):
    startX = random.random() + 1
    #startY = random.random()
    angle = random.vonmisesvariate(0,0)
    
    endX = startX + L*math.cos(angle)
    #endY = startY + L*math.sin(angle)
    diffX = abs(int(startX) - int(endX))
    #print("xb:", startX, "xe:", endX, "=", diffX)
    return diffX > 0


#//////////arguments
arguments = sys.argv

matches = int(sys.argv[1])
length = abs(float(sys.argv[2]))
'''
if length > 1:
    print("AssertionError: L should be smaller then 1")
'''
if len(sys.argv) > 3:
    seed = int(sys.argv[3])
    random.seed(seed)
#/////////
    

    
hits = 0
for i in range(matches):
    if drop_needle(length):
        hits += 1
if hits == 0:
    piEstimate = 0
else:
    probability = hits/matches
    if length <= 1:
        #probability = 2*length/pi -> probability*pi = 2*length -> pi = 2*length/probability
        piEstimate = 2*length/probability
    else:
        #probability = (2*length - 2*(sqrt(l^2-1) + 1/sin(l^-1)))/pi + 1
        # -> pi = 2(length - (sqrt(l^2-1) + 1/sin(l^-1)))/(probability -1)
        sin = math.asin(1/length)
        formula = 2*(length - (math.sqrt(length*length-1) + sin))
        piEstimate = formula/(probability-1)
        


        
print("{0} hits in {1} tries".format(hits, matches))
print("Pi = {0}".format(piEstimate))

    
    

    