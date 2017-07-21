# -*- coding: utf-8 -*-
"""
Created on Tue Jul 11 20:03:10 2017

@author: pfermat
"""

import random

P = [ [0,0.8,0.71,0.83,0.68,0,0.89,0.78,0.56,1,0.62,0.57,1,0.88,1],
[0,0.59,0.39,0.5,0.64,0,0.83,0.54,0.48,1,0.76,0.5,0,0.8,1],
[0,0.69,0.78,0.66,0.63,0,0.88,0.65,0.59,1,0.79,0.54,0,0.75,1],
[0,0.88,0.78,0.9,0.41,0,0.94,0.74,0.83,1,0.76,0.69,0,0.91,1],
[0,0.76,0.78,0.69,0.52,0,0.96,0.7,0.62,1,0.92,0.6,1,0.78,1],
[0,0.78,0.64,0.69,0.55,0,0.92,0.65,0.55,1,0.55,0.51,0,0.78,1],
[0,0.74,0.92,0.52,0.64,0,0.95,0.7,0.56,1,0.93,0.56,0,0.78,1],
[0,0.86,0.93,0.86,0.66,0,0.96,0.91,0.64,1,0.9,0.69,1,0.89,1],
[0,0.9,0.98,0.91,0.36,0,0.97,0.83,0.86,1,0.76,0.72,1,0.88,1],
[0,0.8,0.85,0.83,0.48,0,0.95,0.78,0.81,1,0.93,0.68,1,0.85,1],
[0,0.84,0.74,0.76,0.36,0,0.97,0.74,0.79,1,0.97,0.7,1,0.87,1],
[0,0.81,0.82,0.83,0.64,0,0.96,0.8,0.5,1,0.96,0.67,1,0.88,1],
[0,0.87,0.8,0.74,0.68,0,0.94,0.84,1,1,0.76,0.72,1,0.86,1],
[0,0.71,0.71,0.69,0.41,0,0.9,0.69,0.71,1,0.76,0.56,1,0.78,1],
[0,0.64,0.59,0.71,0.41,0,0.77,0.52,0.56,1,0.55,0.5,1,0.78,0],
[0,0.96,0.85,0.83,0.73,0,1,0.82,0.76,1,0.79,0.65,0,0.84,1],
[0,0.88,0.59,0.64,0.68,0,0.93,0.67,0.55,1,0.79,0.65,1,0.83,1],
[1,0.85,0.81,0.81,0.68,0,0.97,0.91,0.71,1,0.93,0.86,1,0.95,1],
[0,0.61,0.46,0.5,0.61,0,0.84,0.54,0.45,1,0.79,0.48,0,0.76,1],
[0,0.8,0.64,0.79,0.36,0,0.9,0.65,0.52,1,0.74,0.56,1,0.82,1],
[0,0.94,0.97,0.81,0.68,0,0.97,0.92,0.62,1,0.76,0.7,1,0.91,1],
[0,0.85,0.78,0.83,0.64,0,0.89,0.77,0.67,1,0.76,0.68,1,0.9,0],
[0,0.71,0.57,0.52,0.61,0,0.87,0.63,0.33,1,0.76,0.56,1,0.83,1],
[0,0.74,0.57,0.72,0.77,0,0.9,0.69,0.38,1,0.79,0.56,1,0.79,1],
[0,0.76,0.71,0.69,0.59,0,0.9,0.67,0.67,1,0.93,0.63,0,0.85,1],
[0,0.93,0.68,0.69,0.59,0,0.94,0.74,1,1,0.66,0.71,0,0.9,1],
[1,0.88,0.71,0.78,0.77,0,0.96,0.85,0.62,1,0.93,0.88,1,0.95,1],
[0,0.94,0.93,0.91,0.68,0,1,0.97,0.81,1,0.93,0.76,1,0.95,1],
[0,0.78,0.69,0.74,0.77,0,0.91,0.8,0.69,1,0.76,0.59,1,0.82,1],
[0,0.94,0.97,0.91,1,1,1,1,0.81,0,0.93,0.74,1,0.86,1],
[1,0.67,0.56,0.79,0.27,0,0.87,0.56,0.5,1,0.76,0.71,1,0.81,1],
[0,0.89,0.93,0.91,0.55,0,0.99,0.84,0.76,1,0.59,0.62,1,0.78,1],
[0,0.72,0.71,0.52,0.36,0,0.95,0.6,0.43,1,0.79,0.5,1,0.73,1],
[0,0.83,0.74,0.83,0.55,0,0.92,0.77,0.59,1,0.73,0.63,1,0.87,1],
[1,0.9,0.93,1,0.73,0,0.97,0.97,0.69,1,0.93,0.89,1,0.99,1],
[0,0.7,0.73,0.91,0.55,0,0.9,0.8,0.69,0,0.62,0.48,1,0.83,1],
[0,0.85,0.85,0.83,0.68,1,0.99,0.87,0.79,1,0.93,0.8,1,0.89,1],
[0,0.73,0.69,0.6,0.36,0,0.87,0.6,0.83,1,0.48,0.57,1,0.8,1],
[1,0.79,0.91,0.93,0.55,0,0.96,0.83,0.48,1,1,0.79,1,0.87,1],
[0,0.74,0.73,0.81,0.73,0,0.86,0.79,0.45,1,0.76,0.66,1,0.91,0],
[0,0.86,0.88,0.81,0.68,0,0.96,0.9,0.81,1,0.93,0.66,1,0.87,1],
[0,0.82,0.71,0.83,0.55,0,0.92,0.81,0.81,1,0.83,0.71,1,0.91,1],
[0,0.79,0.64,0.76,0.63,0,0.93,0.63,0.48,1,0.83,0.56,0,0.75,1],
[0,0.98,0.92,0.83,0.55,0,1,0.84,0.81,1,0.76,0.7,1,0.88,1],
[1,0.73,0.51,0.85,0.36,1,0.93,0.56,0.5,0,0.81,0.65,1,0.78,1],
[0,0.85,0.92,0.83,0.68,0,0.98,0.88,0.74,1,0.93,0.76,1,0.9,1],
[0,0.84,0.66,0.78,0.55,0,0.9,0.66,0.56,1,0.76,0.6,0,0.83,1],
[0,0.82,0.78,0.69,0.64,0,0.89,0.74,0.62,1,0.93,0.67,1,0.9,0],
[0,0.83,0.98,0.9,0.77,1,1,0.97,0.83,1,0.6,0.72,1,0.81,1],
[0,0.94,0.97,0.91,0.86,0,0.99,1,0.86,1,0.79,0.76,1,0.92,1],
[0,0.81,0.98,0.91,0.55,0,0.94,0.87,0.56,1,0.93,0.64,1,0.9,1],
[0,0.69,0.83,0.69,0.55,0,0.92,0.73,0.36,1,0.62,0.5,1,0.78,1],
[0,0.82,0.73,0.81,0.64,0,0.87,0.73,0.56,1,0.93,0.71,1,0.94,0],
[0,0.93,0.86,0.91,0.68,0,0.99,0.95,0.81,1,0.76,0.73,1,0.93,1],
[0,0.74,0.78,0.79,0.36,0,0.88,0.71,0.62,1,0.76,0.55,1,0.84,1] ]

#P = [ [0.5,0.5], [0.4,0.4], [0.37,0.37], [0.65,0.65], [0.82,0.82] ]

dim = 15    # 点的维数
n = 55      # 点的数量
pm = 0.3    # 变异概率
popu = 3000 # 种群数量
r = 0.2     # 交叉参数
gene = 200  # 迭代代数

class Chrom(object):
    def __init__(self):
        self.a = []
        self.b = 0
        
        for i in range(dim):
            self.a.append(random.uniform(-1,1))
            
        self.b = random.uniform(-10,10)
        
    def mutation(self):
        for i in range(dim):
            if random.uniform(0,1) <= pm:
                self.a[i] = random.uniform(-1,1)
                
        if random.uniform(0,1) <= pm:
            self.b = random.uniform(-10,10)
            
    @staticmethod
    def cross(x, y) -> list:
        tmp_a = Chrom()
        tmp_b = Chrom()
        
        for i in range(dim):
            tmp_a.a[i] = r*x.a[i] + (1-r)*y.a[i]
            tmp_b.a[i] = (1-r)*x.a[i] + r*y.a[i]
            
        tmp_a.b = r*x.b + (1-r)*y.b
        tmp_b.b = (1-r)*x.b + r*y.b
        
        return [tmp_a, tmp_b]
    
    def eval(self) -> float:
        f = 0.0
        for i in range(n):
            s = 0.0
            for j in range(dim):
                s += self.a[j] * P[i][j]
            s += self.b
            f += s*s
        
        suma = 0.0
        for i in range(dim):
            suma += self.a[i] * self.a[i]
            
        return f/suma

def select(plist:list) -> int:
    r = random.uniform(0,1)
    sum = 0.0
    for i in range(len(plist)):
        sum += plist[i]
        if r <= sum:
            return i

def main():
    # 初始化种群
    data = []
    for i in range(popu):
        data.append(Chrom())
        
    # 迭代
    for g in range(gene):
        # 计算每个个体的评价函数
        f = []
        fsum = 0.0
        for i in range(popu):
            f.append(data[i].eval())
            fsum += f[i]
        # 计算每个个体被选中的概率
        fp = []
        for i in range(popu):
            fp.append(f[i]/fsum)
        
        # 交叉产生新个体
        data_tmp = []
        for i in range(popu):
            index1 = select(fp)
            index2 = select(fp)
            new_chroms = Chrom.cross(data[index1], data[index2])
            data_tmp.extend(new_chroms)
            
        # 变异
        for i in range(4, popu):
            data[i].mutation()
            
        # 根据评价函数排序
        data_all = []
        data_all.extend(data)
        data_all.extend(data_tmp)
        data_all.sort(key=lambda chrom:chrom.eval())
        
        # 清除原有种群 将排序后的新种群写入
        data.clear()
        for i in range(popu):
            data.append(data_all[i])
            
        print("Gene", g, ":", data[0].eval())
    
    print(data[0].a, data[0].b)
    
if __name__ == '__main__':
    main()