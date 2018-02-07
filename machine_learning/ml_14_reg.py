import random
import numpy as np
from scipy.linalg import pinv


def sign(x1, x2):
 	ret = x1*x1 + x2*x2 -0.6		
	ret = 1.0 if ret >= 0.0 else -1.0
	return ret

toterr = 0

for _ in range(1000):

	dataNEW = []
	datalabelNEW  = []
	data = []
	datalabel  = []

	for i in range(1000):
		x1 = random.uniform(-1.0,1.0)
		x2 = random.uniform(-1.0,1.0)
		data.append([1, x1, x2, x1*x2, x1*x1, x2*x2])
	
		label = sign(x1, x2)
		label = label * -1 if random.random() < 0.1 else label 
		datalabel.append([label])

	for i in range(1000):
		x1 = random.uniform(-1.0,1.0)
		x2 = random.uniform(-1.0,1.0)
		dataNEW.append([1, x1, x2, x1*x2, x1*x1, x2*x2])
	
		label = sign(x1, x2)
		label = label * -1 if random.random() < 0.1 else label 
		datalabelNEW.append([label])

	x = np.array(data)
	y = np.array(datalabel)
	wlin = pinv(x).dot(y)

	xNEW = np.array(dataNEW)
	yNEW = np.array(datalabelNEW)
	y_hat = xNEW.dot(wlin)
	
	err = 0 
	for i in range(1000):
		y_hat_item = y_hat.item((i,0))
		y_hat_label = 1.0 if y_hat_item >= 0 else -1.0
		if yNEW.item((i,0)) != y_hat_label:
			err += 1

	toterr +=  float(err) / 1000

print toterr /1000
