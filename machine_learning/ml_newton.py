import math
import numpy as np
from numpy.linalg import inv

def le(le0):
	u = le0.item((0,0))
	v = le0.item((1,0))
	lu = math.exp(u) + v*math.exp(u*v) + 2*u -2*v - 3 
	lv = 2*math.exp(2*v) + u*math.exp(u*v) -2*u + 4*v -2
	lu2 = math.exp(u) + math.pow(v,2)*math.exp(u*v) + 2 
	lv2 = 4*math.exp(2*v) + math.pow(u,2)*math.exp(u*v) + 4
	luv = u*v*math.exp(u*v) -2
	
	le2 = inv( np.array([[lu2,luv],[luv,lv2]]) )
	le = np.array([[lu],[lv]])
	return  -np.multiply(le2,le)

le0 = np.array([[0],[0]])

for i in range(5):
	le0 = le0 + le(le0) 

u = le0.item((0,0))
v = le0.item((1,0))

ans = math.exp(u) + math.exp(2*v) + math.exp(u*v) + math.pow(u,2) - 2*u*v +\
	2*math.pow(v,2) -3*u -2*v

print ans
