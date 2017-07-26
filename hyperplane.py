# -*- coding: utf-8 -*-
"""
Created on Wed Jul 26 12:52:57 2017

@author: pfermat
"""

import copy
import math
import numpy as np
np.set_printoptions(threshold=np.inf)

def lsm(plist:list) -> np.matrix:
    n = len(plist)
#    dim = len(plist[0])
    ly = []
    p = copy.deepcopy(plist)
    
    for i in range(n):
        ly.append(plist[i][0])
    y = np.matrix(ly)
    
    for i in range(n):
        p[i][0] = 1
    a = np.matrix(p)
    
    return np.linalg.pinv(a) * y.T

def coe_p(p:list) -> list:
    result = lsm(p).T.tolist()[0]
    return coe_calc(result)

def coe_m(m:np.matrix) -> list:
    result = m.T.tolist()[0]
    return coe_calc(result)

def coe_calc(result:list) -> list:
    b = result[0]
    a = [-1,]
    for i in range(1, len(result)):
        a.append(result[i])
        
    l = []
    l.append(a)
    l.append(b)
    return l

def d(p:list) -> list:
    f = 0.0
    n = len(p)
    dim = len(p[0])
    coe = coe_p(p)
    a = coe[0]
    b = coe[1]
    d_p = []
    result = []
    
    for i in range(n):
        d = 0.0
        for j in range(dim):
            d += a[j] * p[i][j]
        d += b
        
        suma = 0.0
        for j in range(dim):
            suma += a[j] * a[j]
            
        d_p.append(d/math.sqrt(suma))
        f += d*d/suma
        
    result.append(d_p)
    result.append(f)
    return result