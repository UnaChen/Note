import numpy as np

data = []
for x1, x2 in [(1.0, 1.0), (1.0, -1.0), (-1.0, -1.0), (-1.0, 1.0), (0.0, 0.0), (1.0, 0.0)]:
	data.append(np.array([1.0,x1,x2,x1*x2,x1*x1,x2*x2]))

labels = []
def gen_labels(l, lables):
	if len(l) == 6:
		labels.append(l)
	else:
		gen_labels(l + [1.0], labels)
		gen_labels(l + [-1.0], labels)

def sign(x):
	return 1.0 if x >= 0 else -1.0 

gen_labels([], labels)

for label in labels:
	w0 = np.array([0.0] * 6)

	i = 0
	corr = 0 
	print label
	while 1:
		if sign(np.inner(data[i], w0)) != label[i]:
			w0 = np.add(w0, label[i] * data[i])
			corr = 0 
		else:
			corr += 1
		if corr == 6: break
		i = (i + 1) % 6
	
	print w0	
	
