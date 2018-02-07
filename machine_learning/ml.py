import math

def le(u, v):
	lu = math.exp(u) + v*math.exp(u*v) + 2*u -2*v - 3 
	lv = 2*math.exp(2*v) + u*math.exp(u*v) -2*u + 4*v -2
	return lu, lv

u = 0
v = 0

for i in range(5):
	lu, lv = le(u, v)
	u = u - 0.01* lu
	v = v - 0.01* lv

ans = math.exp(u) + math.exp(2*v) + math.exp(u*v) + math.pow(u,2) - 2*u*v +\
	2*math.pow(v,2) -3*u -2*v

print ans
