# -*- coding: utf-8 -*-
"""
Created on Wed Aug  9 11:24:15 2017

@author: pfermat
"""

import math
from scipy.sparse import dok_matrix

#count = 5
#treedata = ( (0,1), (0,2), (1,3), (2,3), (2,4) )
#
#dm = dok_matrix( (count, count), dtype = bool )
#for e in treedata:
#    dm[e[0], e[1]] = True

def GetMax(data:tuple) -> int:
    maxium = 0
    for e in data:
        maxium = max(e[0], e[1], maxium)
            
    return maxium

class Kdata(object):
    def __init__(self, treedata:tuple, max:int):
        #self.count = GetMax(treedata)
        self.count = max
        self.dm = dok_matrix( (self.count, self.count), dtype = bool )
        for e in treedata:
            self.dm[e[0], e[1]] = True
            
    def GetPost(self, index:int) -> list:
        l = []
        for i in range(self.dm.shape[0]):
            if self.dm[index, i]:
                l.append(i)
                
        return l
    
    def GetPre(self, index:int) -> list:
        l = []
        for i in range(self.dm.shape[0]):
            if self.dm[i, index]:
                l.append(i)
                
        return l

def CompCheck(k:Kdata, data:list) -> bool:
    for index in data:
        for e in k.GetPost(index):
            if e not in data:
                return False
    
    return True

def BasicCompCheck(k:Kdata, data:list) -> bool:
    precount = 0
    for index in data:
        for e in k.GetPre(index):
            if e not in data:
                precount += 1
                if precount >= 2:
                    return False
                
    return True
    
def StatusToIndex(k:Kdata, status:int) -> list:
    l = []
    for i in range(k.count):
        if status & (1 << i):
            l.append(i)
            
    return l  

def Component(k:Kdata) -> list:
    l = []
    for i in range(1, int(math.pow(2, k.count))):
        index = StatusToIndex(k, i)
        if CompCheck(k, index):
            l.append(index)
            
    return l

def BasicComponent(k:Kdata) -> list:
    l = []
    comp = Component(k)
    for e in comp:
        if BasicCompCheck(k, e):
            l.append(e)
            
    return l

def main():
    tree = ( (0,1), (0,2), (1,3), (2,4), (2,3) )
    k = Kdata(tree, 5)
    bc = BasicComponent(k)
    print(bc)
    
if __name__ == '__main__':
    main()