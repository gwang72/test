from math import exp, log
from ga import Chrom


class Item(object):
    """
    IRT模型M-2PPC中的一个被试项目
    具体模型定义参见bmirt
    """
    def __init__(self, index: int, data: list):
        """

        :param index: 项目编号
        :param data: 项目参数
        """
        self.index = index
        self.Kj = int(data[0])
        self.beta_2j = float(data[1])
        self.beta_delta_j = {}

        self.beta_delta_j[1] = 0.0
        for i in range(2, self.Kj + 1):
            self.beta_delta_j[i] = float(data[i])


    def pk(self, theta: float) -> dict:
        d = {}

        for response in range(1, self.Kj + 1):
            d[response] = numerator(response, self.beta_2j, theta, self.beta_delta_j) / sum_denominator(self.Kj, self.beta_2j, theta, self.beta_delta_j)

        return d


    def EX(self, theta: float) -> float:
        dpk = self.pk(theta)
        sum = 0.0
        for k, v in dpk.items():
            sum += (k - 1) * v

        return sum


    def getParams(self) -> dict:
        d = {}

        d[1] = self.beta_2j
        for i in range(2, self.Kj + 1):
            d[i] = self.beta_delta_j[i]

        return d


def sum_beta_delta(m: int, beta_delta: dict) -> float:
    sum = 0.0
    for i in range(1, m + 1):
        sum += beta_delta[i]

    return sum


def denominator(m: int, beta_2: float, theta: float, beta_delta: dict) -> float:
    return exp((m - 1) * beta_2 * theta - sum_beta_delta(m, beta_delta))


def sum_denominator(K: int, beta_2: float, theta: float, beta_delta: dict) -> float:
    sum = 0.0
    for i in range(1, K + 1):
        sum += denominator(i, beta_2, theta, beta_delta)

    return sum


def numerator(k: int, beta_2: float, theta: float, beta_delta: dict) -> float:
    return exp((k - 1) * beta_2 * theta - sum_beta_delta(k, beta_delta))


def P_ijk(k: int, Kj: int, beta_2j: float, theta: float, beta_delta_j: dict) -> float:
    numer = numerator(k, beta_2j, theta, beta_delta_j)
    denom = sum_denominator(Kj, beta_2j, theta, beta_delta_j)

    return numer / denom


def delta(X_ij: int, k: int) -> bool:
    if X_ij == k:
        return True
    else:
        return False


def logP(N: int, J: int, KJ: dict, X_ij: dict, thetas: dict, params: dict, item: 'Chrom') -> float:
    sum = 0.0
    for i in range(1, N + 1):
        for j in range(1, J + 1):
            for k in range(1, KJ[j] + 1):
                # 第j题的beta_2j
                beta_2j = item.getAllBeta()[j][1]
                # 第j题的beta_delta_j
                beta_delta_j = item.getAllBeta()[j]
                sum += P_ijk(k, KJ[j], beta_2j, thetas[i], beta_delta_j) if delta(X_ij[i][j], k - 1) == True else 0

    return sum
