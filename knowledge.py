# -*- coding: utf-8 -*-
"""
Created on Wed Aug  9 11:24:15 2017

@author: pfermat
"""

import math
from scipy.sparse import dok_matrix

class Kdata(object):
    """
    有向图的邻接矩阵
    dm[i,j]表示节点i到节点j有一条边
    """
    def __init__(self, treedata:tuple):
        self.result = []
        self.count = GetMax(treedata)
        self.dm = dok_matrix( (self.count, self.count), dtype = bool )
        for e in treedata:
            self.dm[e[0], e[1]] = True
            
    def GetPost(self, index:int) -> list:
        """
        得到节点index的所有后继节点
        """
        l = []
        for i in range(self.dm.shape[0]):
            if self.dm[index, i]:
                l.append(i)
                
        return l
    
    def GetPre(self, index:int) -> list:
        """
        得到节点index的所有前置节点
        """
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
        """
        根据给定的起始节点start和终止节点end，寻找所有路径
        """
        self.result.clear()
        visited = [False] * (self.count)
        path = []
        self.SearchUtil(start, end, visited, path)
        
        return self.result

def GetMax(data:tuple) -> int:
    """
    根据节点边的输入数据，寻找最大节点编号+1
    即节点数量，假设最小节点为0，最大节点为N，且连续编号
    """
    maxium = 0
    for e in data:
        maxium = max(e[0], e[1], maxium)
            
    return maxium+1

def CompCheck(k:Kdata, data:list) -> bool:
    """
    检查是否为知识组件
    """
    for index in data:
        for e in k.GetPost(index):
            if e not in data:
                return False
    
    return True

def BasicCompCheck(k:Kdata, data:list) -> bool:
    """
    检查是否为基本知识组件
    """
    precount = 0
    for index in data:
        for e in k.GetPre(index):
            if e not in data:
                precount += 1
                if precount >= 2:
                    return False
                
    return True
    
def StatusToIndex(k:Kdata, status:int) -> list:
    """
    将二进制状态码status转换为节点编号
    如：0b10110 ==> [1,2,4]
    """
    l = []
    for i in range(k.count):
        if status & (1 << i):
            l.append(i)
            
    return l  

def Component(k:Kdata) -> list:
    """
    找出所有知识组件
    """
    l = []
    for i in range(1, int(math.pow(2, k.count))):
        if i % 10000 == 0:
            print(i/100, '%')
        index = StatusToIndex(k, i)
        if CompCheck(k, index):
            l.append(index)
            
    return l

def BasicComponent(k:Kdata) -> list:
    """
    找出所有基本知识组件
    """
    l = []
    comp = Component(k)
    for e in comp:
        if BasicCompCheck(k, e):
            l.append(e)
            
    return l

def ListToDict(l:list) -> dict:
    """
    将list转换为dict，dict.key为从0开始的编号
    如：[2,3,5] ==> {0:2, 1:3, 2:5}
    """
    d = {}
    for i in range(len(l)):
        d[i] = l[i]
        
    return d

def MaxLen(d:dict) -> int:
    """
    寻找dict中知识点数量最多的元素
    此处dict为 { 数字编号:[知识点] } 的形式
    """
    max = 1
    for e in d.values():
        if len(e) > max:
            max = len(e)
            
    return max

def MinLen(d:dict) -> int:
    """
    寻找dict中知识点数量最少的元素
    此处dict为 { 数字编号:[知识点] } 的形式
    """
    min = 999
    for e in d.values():
        if len(e) < min:
            min = len(e)
            
    return min

def Sort(d:dict) -> list:
    """
    *首先需要将知识组件列表通过ListToDict函数转换为dict参数
    将所有知识组件按照其中所含知识点数量从少到多排列分层
    输出格式为：
    [
    { 数字编号:[知识点],  # 此处为知识组件
      数字编号:[知识点],
      ...
    },  # 此dict为同一层的知识组件，其中所含的知识点数量相等
    {...},
    ...
    ]
    """
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
    """
    判断ly是否只比lx多一个元素
    """
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
    """
    输入为使用Sort函数排序后的知识组件
    遍历每一层，将当前层与后一层进行比较，寻找出所有知识点递进的知识组件(见IsDelta函数)
    将它们的关系看成一条边
    """
    t = []
    for i in range(len(l)-1):
        for kx,vx in l[i].items():
            for ky,vy in l[i+1].items():
                if IsDelta(vx, vy):
                    t.append((kx, ky))
                    
    return tuple(t)

def FindMinContain(comp:list, k:int) -> list:
    """
    在知识组件列表中寻找包含指定知识点k，且长度最小的知识组件
    """
    minlen = 999
    mincomp = []
    for e in comp:
        if k in e:
            if len(e) < minlen:
                minlen = len(e)
                mincomp = e.copy()
                
    return mincomp

def FindMinSort(scomp:list, k:int) -> dict:
    """
    在Sort函数排序后的知识组件中，寻找包含指定知识点k，且长度最小的知识组件
    """
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
    """
    在Sort函数排序后的知识组件中，寻找包含指定知识点列表ks，且长度最小的知识组件
    """
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
    """
    判断check是否包含于source
    TODO:应该也可以用集合运算实现
    """
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