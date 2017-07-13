import numpy as np
import multiperceptron as mp

import math
import random

Eta = 1.0

n_sample = 10
n_test_sample = 2000

X = []
y = []

for i in range(n_sample):
    v = [random.random(), random.random()]
    dtype = random.randrange(0,2)

    v[0] *= math.pi
    v[1] = math.sqrt(49 + 51 * v[1])
    if dtype > 0:
        (v[0], v[1]) = (v[1] * math.cos(v[0]), v[1] * math.sin(v[0]))
    else:
        (v[0], v[1]) = (v[1] * math.cos(v[0] + math.pi), v[1] * math.sin(v[0] + math.pi))
        v[0] += 8
        v[1] += 3
    X.append(v)
    y.append(dtype)
    
X = np.array(X)
y = np.array(y)

ppn = mp.MultiPerceptron(eta=Eta, n_iter=10)

ppn.fit(X,y)
