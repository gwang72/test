import irt
import read
import random
import profile


PM = 0.1  # 变异概率
PC = 0.9  # 交叉概率
POPU = 50  # 种族数量
r = 0.2  # 交叉参数
GENE = 10  # 迭代次数
tour = 2  # 锦标赛选择方法中一次选取的个体数量

max_theta = 4.0  # 能力值上下限
max_beta = 20.0  # 题目难度上下限
max_dis = 1.0  # 题目区分度上下限

class Chrom(object):
    def __init__(self, N: int, KJ: dict):
        self.thetas = {}  # theta数组
        self.betas = {}  # beta数组
        self.N = 0  # 被试者数量
        self.KJ = {}  # 题目的KJ参数
        count = 0  # beta参数的个数
        index = 0

        self.N = N
        for k, v in KJ.items():
            count += v
            self.KJ[k] = v

        for i in range(1, N + 1):
            self.thetas[i] = random.uniform(-max_theta, max_theta)

        for v in KJ.values():
            for i in range(1, v + 1):
                index += 1
                if i == 1:
                    value = random.uniform(-max_dis, max_dis)
                else:
                    value = random.uniform(-max_beta, max_beta)
                self.betas[index] = value


    def getAllBeta(self) -> dict:
        d = {}
        index = 0

        for k, v in self.KJ.items():
            tmp = {}
            for i in range(1, v + 1):
                index += 1
                tmp[i] = self.betas[index]
            d[k] = tmp

        return d


    def mutation(self):
        index = random.randint(1, self.N + len(self.betas))
        if index <= self.N:
            self.thetas[index] = random.uniform(-max_theta, max_theta)
        elif index == self.N + 1:
            self.betas[1] = random.uniform(-1, 1)
        else:
            self.betas[index - self.N] = random.uniform(-max_beta, max_beta)


    def fitness(self, X_ij: dict) -> float:
        #print("fitness in")
        return irt.logP(self.N, len(self.KJ), self.KJ, X_ij, self.thetas, self.betas, self)


def select(population: list, X_ij: dict) -> tuple:
    count = len(population)
    competitors_1 = random.sample(range(count), tour)
    competitors_2 = random.sample(range(count), tour)

    father = max([val for idx, val in enumerate(population) if idx in competitors_1], key=lambda chrom: chrom.fitness(X_ij))
    mother = max([val for idx, val in enumerate(population) if idx in competitors_2], key=lambda chrom: chrom.fitness(X_ij))

    return (father, mother)


def cross(g1: 'Chrom', g2: 'Chrom') -> tuple:
    new_g1 = Chrom(g1.N, g1.KJ)
    new_g2 = Chrom(g1.N, g1.KJ)

    for i in range(1, g1.N + 1):
        new_g1.thetas[i] = r * g1.thetas[i] + (1 - r) * g2.thetas[i]
        new_g2.thetas[i] = (1 - r) * g1.thetas[i] + r * g2.thetas[i]

    for i in range(1, len(g1.betas)):
        new_g1.betas[i] = r * g1.betas[i] + (1 - r) * g2.betas[i]
        new_g2.betas[i] = (1 - r) * g1.betas[i] + r * g2.betas[i]

    return (new_g1, new_g2)


def main():
    # 试题与被试者参数
    paper_N = 166  # 541
    paper_KJ = {}
    X_ij = {}
    data = read.read_csv('paper1.csv')
    item_count = len(data[0])

    for i in range(1, item_count + 1):
        paper_KJ[i] = int(data[0][i - 1])

    for i in range(1, paper_N + 1):
        tmp = {}
        count = 0
        for j in range(1, item_count + 1):
            tmp[j] = int(data[i][j - 1])

        X_ij[i] = tmp

    # 产生初始种群
    population = []
    for i in range(POPU):
        population.append(Chrom(paper_N, paper_KJ))

    # 迭代
    for g in range(GENE):
        new_population = []
        for i in range(int(POPU/2)):
            # 选择
            print("select", i)
            a, b = select(population, X_ij)
            if random.random() <= PC:
                # 交叉
                new_a, new_b = cross(a, b)
                # 将新个体存入新种群
                new_population.extend([new_a, new_b])
            else:
                new_population.extend([a, b])

        # 变异
        # for i in range(POPU):
        #     if random.random() <= PM:
        #         new_population[i].mutation()

        # 将原来的种群替代
        population = new_population[:]

        # 根据评价函数列出最小者
        # new_population.sort(key=lambda chrom:chrom.fitness(X_ij))
        max_chrom = max(new_population, key=lambda chrom:chrom.fitness(X_ij))
        print("Gene", g)
        print("fitness", max_chrom.fitness(X_ij))
        print("thetas", max_chrom.thetas)
        print("betas", max_chrom.betas)


if __name__ == '__main__':
    main()
