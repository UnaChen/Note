import numpy as np
import math

def read_data(fname):
    X = []
    Y = []
    with open(fname) as fd:
        for row in fd:
            row = row.strip("\n").strip(" ")
            tokens = row.split(" ")
            xn = np.array([1.0] +  [float(t) for t in tokens[:20]])
            X.append(xn)
            Y.append(float(tokens[20]))
    return X, Y

theta = lambda v: 1.0 / (1.0 + math.exp(-v))

def grad(w, xn, yn):
    ywx = -1.0 * yn * np.inner(w, xn)
    return (theta(ywx) * -yn) * xn

def grad_s(w, X, Y):
    s = np.array([0] * 21)
    for x, y in zip(X, Y):
        s = np.add(s, grad(w, x, y))
    s = s / len(Y)
    #print s
    return s

def h(w, x):
    return 1.0 / (1.0 + math.exp(-np.inner(w, x)))

#def main():
#    X, Y = read_data("hw3_train.dat")
#    step = 0.01
#    T = 2000
#    w = np.array([0] * 21)
#    for i in range(T):
#        w = w - step * grad_s(w, X, Y)
#    print w
#    val_X, val_Y = read_data("hw3_test.dat")
#    err_cnt = 0.0
#    for x, y in zip(val_X, val_Y):
#        pre_y = 1.0 if h(w, x) >= 0.5 else -1.0
#        if pre_y != y:
#            err_cnt += 1.0
#    print "{0}".format(err_cnt/len(val_Y))

def main():
    X, Y = read_data("hw3_train.dat")
    step = 0.001
    T = 2000
    w = np.array([0] * 21)
    i = 0
    while T > 0:
        w = w - step * grad(w, X[i], Y[i])
        i = (i + 1) % len(Y)
        T = T - 1
    val_X, val_Y = read_data("hw3_test.dat")
    err_cnt = 0.0
    for x, y in zip(val_X, val_Y):
        pre_y = 1.0 if h(w, x) >= 0.5 else -1.0
        if pre_y != y:
            err_cnt += 1.0
    print "{0}".format(err_cnt/len(val_Y))

if __name__ == "__main__":
    main()
