import numpy as np
import math

with open("./hw3_train.dat", 'r') as f:
	c = f.readlines()
	datastr = [cc.strip('\n').strip(' ').split(' ') for cc in c]
	datalabel = [ float(d[-1]) for d in datastr]
	data = [ [1.0]+[float(dd) for dd in d[:-1]] for d in datastr]

with open("./hw3_test.dat", 'r') as f:
	c = f.readlines()
	datastr = [cc.strip('\n').strip(' ').split(' ') for cc in c]
	datalabel_T = [ float(d[-1]) for d in datastr]
	data_T = [ [1.0]+[float(dd) for dd in d[:-1]] for d in datastr]

x = []
for i in range(len(data)):
	x.append(np.array(data[i]))

xT = []
for i in range(len(data_T)):
	xT.append(np.array(data_T[i]))

def func(y, w, x):	
	return 1.0/(1.0 + math.exp(-(-np.inner(w,x)* y))) * (-y*x)


w0 = np.array([0.0]*21)

for i in range(2000):
	ein = np.array([0.0] * 21)
	rand = i % len(data)
	ein =  np.add(ein, func( datalabel[rand], w0, x[rand]))
	
	w0 = w0 - 0.001 * ein
print w0
eout = 0
for i in range(len(data_T)):
	y_hat = 1.0 / (1+ math.exp(-1.0* np.inner(w0, xT[i])))
	y_hat = 1.0 if y_hat >= 0.5 else -1.0
	if datalabel_T[i] != y_hat:
		eout += 1

print float(eout)/len(data_T)
