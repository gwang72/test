# -*- coding: utf-8 -*-
"""
Created on Wed Aug  9 11:24:15 2017

@author: pfermat
"""

import math
from scipy.sparse import dok_matrix

class Kdata(object):
    def __init__(self, treedata:tuple):
        self.result = []
        self.count = GetMax(treedata)
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
    
    def SearchUtil(self, start:int, end:int, visited:list, path:list):
        visited[start] = True
        path.append(start)
    
        if start == end:
            self.result.append(path.copy())
        else:
            for i in self.GetPost(start):
                if visited[i] == False:
                    self.SearchUtil(i, end, visited, path)
                    
        path.pop()
        visited[start] = False
                    
    def Search(self, start:int, end:int) -> list:
        self.result.clear()
        visited = [False] * (self.count)
        path = []
        self.SearchUtil(start, end, visited, path)
        
        return self.result

def GetMax(data:tuple) -> int:
    maxium = 0
    for e in data:
        maxium = max(e[0], e[1], maxium)
            
    return maxium+1

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
        if i % 10000 == 0:
            print(i/100, '%')
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

def ListToDict(l:list) -> dict:
    d = {}
    for i in range(len(l)):
        d[i] = l[i]
        
    return d

def MaxLen(d:dict) -> int:
    max = 1
    for e in d.values():
        if len(e) > max:
            max = len(e)
            
    return max

def MinLen(d:dict) -> int:
    min = 999
    for e in d.values():
        if len(e) < min:
            min = len(e)
            
    return min

def Sort(d:dict) -> list:
    l = []
    tmp = {}
    min = MinLen(d)
    max = MaxLen(d)
    for i in range(min, max+1):
        for k,v in d.items():
            if len(v) == i:
                tmp[k] = v
        l.append(tmp.copy())
        tmp.clear()
        
    return l

def MaxKey(l:list) -> int:
    max = 0
    for d in l:
        if max(d.keys()) > max:
            max = max(d.keys())
            
    return max

def IsDelta(lx:list, ly:list) -> bool:
    lenx = len(lx)
    leny = len(ly)
    if leny - lenx != 1:
        return False
    
    setx = set(lx)
    sety = set(ly)
    inter = setx.intersection(sety)
    if len(inter) != lenx:
        return False
    
    return True

def MapTuple(l:list) -> tuple:
    t = []
    for i in range(len(l)-1):
        for kx,vx in l[i].items():
            for ky,vy in l[i+1].items():
                if IsDelta(vx, vy):
                    t.append((kx, ky))
                    
    return tuple(t)

def FindMinContain(comp:list, k:int) -> list:
    minlen = 999
    mincomp = []
    for e in comp:
        if k in e:
            if len(e) < minlen:
                minlen = len(e)
                mincomp = e.copy()
                
    return mincomp

def FindMinSort(scomp:list, k:int) -> dict:
    minlen = 999
    mincomp = []
    for dicts in scomp:
        for key,val in dicts.items():
            if k in val:
                if len(val) < minlen:
                    minlen = len(val)
                    mincomp = val.copy()
                    minnum = key
    
    return { minnum : mincomp }

def FindMinSortL(scomp:list, ks:list) -> dict:
    minlen = 999
    mincomp = []
    for dicts in scomp:
        for key,val in dicts.items():
            if IsAllContain(ks, val):
                if len(val) < minlen:
                    minlen = len(val)
                    mincomp = val.copy()
                    minnum = key
                    
    return { minnum : mincomp }

def IsAllContain(check:list, source:list) -> bool:
    if len(check) > len(source):
        return False
    
    for e in check:
        if e not in source:
            return False
        
    return True

def main():
    tree = ( (0,1), (1,2), (2,3), (2,4), (2,5), (1,6), (6,7), (6,8), (8,3) )#, (0,9), (9,10), (10,11), (10,12), (10,13), (9,14), (14,15), (14,16), (14,17), (14,18), (14,19), (15,18), (15,19) )
    k = Kdata(tree)
    c = Component(k)
    print("component", c)
    #print("min contain", FindMinContain(c, 2))
    s = Sort(ListToDict(c))
    print("sorted", s)
    #print("min contain", FindMinSort(s, 2))
    #print("min contain", FindMinSortL(s, [2,3,4,5,6,8]))
    t = MapTuple(s)
    #print(t)
    tree = t
    k = Kdata(tree)
    #allpath = k.Search(15, 33)
    #print(allpath)

if __name__ == '__main__':
    main()