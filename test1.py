# NOT TO EDIT
#pointLoads = np.array([[]]) #point forces (location, xMag, yMag)

# INPUT SPAN AND FORCE DATA 
span = 17
A = 3 #distance of A support from the left
B = 13 #distance of B support form the left

# DEPENDENCIES & DEAFULTS
import math 
import numpy as np

# INPUT FORCE DATA
pointLoads = np.array([[6, 0, -90]])
print ("size of array is: ", pointLoads.size)
print ("dimensions of array are: ", pointLoads.ndim)
print ("shape of array is: ", pointLoads.shape)
print (pointLoads)
print (pointLoads[0, 0])
print (pointLoads[0, 1])
print (pointLoads[0, 2])
#print(pointLoads[0,2])
pointMoments = np.array([[17,50]])
linearLoads = np.array([[8, 17, -10, 0]])
print(pointLoads)

# Defaults and initialisations
diva = 10000 #divide the span up to into this number of data points
delta = span/diva #distance between data points
X = np.arange(0, span + delta, delta) #range of X-coordinates
nPL = len (pointLoads[0])
#print (nPL)

reactions = np.array([0.0, 0, 0])
shearForce = np.empty ([0, len (X)])
bendingMoment = np.empty ([0, len (X)])

# NOT EDIT
pointLoads = np.array([[]]) #point forces (location, xMag, yMag)

# REACTION CALCULATION

def reactions_PL(n):
    xp = pointLoads[n, 0]
    fx = pointLoads[n, 1]
    fy = pointLoads[n, 2]
    
    la_p = A-xp
    mp = fy*la_p
    la_vb = B-A
    
    Vb = mp/la_vb
    Va = -fy-Vb
    Ba = -fx
    
    return Va, Vb, Ha
    

PL_record = np.empty ([0,3])
if (nPL>0):
    for n, p in enumerate(pointLoads):
        #print (enumerate(pointLoads))
        va, vb, ha = reactions_PL(n) #Calculate reactions
        PL_record = np.append(PL_record, [np.array([va, ha, vb])], axis=0)
        
        reactions[0] = reactions[0] + va
        reactions[1] = reactions[1] + ha
        reactions[2] = reactions[2] + vb
    
# PLOTTING AND PRINTING 
print ("The vertical reaction at A is (one) kN", format(one = round(reactions[0],2)))
print ("The vertical reaction at B is (one) kN", format(one = round(reactions[2],2)))
print ("The horizontal reaction at A is (one) kN", format(one = round(reactions[1],2)))