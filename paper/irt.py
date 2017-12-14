from numpy import exp
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
        self.sum_beta = {}

        self.beta_delta_j[1] = 0.0
        for i in range(2, self.Kj + 1):
            self.beta_delta_j[i] = float(data[i])

        for i in range(1, max(self.beta_delta_j.keys()) + 1):
            self.sum_beta[i] = self.sum_beta_delta(i, self.beta_delta_j)

    def pk(self, theta: float) -> dict:
        d = {}

        for response in range(1, self.Kj + 1):
            d[response] = self.numerator(response, theta) / self.sum_denominator(self.Kj, theta)

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

    def sum_beta_delta(self, m: int, beta_delta_j: dict) -> float:
        sum = 0.0
        for i in range(1, m + 1):
            sum += beta_delta_j[i]

        return sum

    def denominator(self, m: int, theta: float) -> float:
        return exp((m - 1) * self.beta_2j * theta - self.sum_beta[m])

    def sum_denominator(self, K: int, theta: float) -> float:
        sum = 0.0
        for i in range(1, K + 1):
            sum += self.denominator(i, theta)

        return sum

    def numerator(self, k: int, theta: float) -> float:
        return exp((k - 1) * self.beta_2j * theta - self.sum_beta[k])

    def P_ijk(self, k: int, theta: float) -> float:
        numer = self.numerator(k, theta)
        # TODO 此处应该是sum_denominator
        denom = self.denominator(self.Kj, theta)

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
                allbeta_j = item.getAllBeta()[j]
                data = []
                data.append(KJ[j])
                data.append(allbeta_j[1])
                data.extend(list(allbeta_j.values()))
                tmp_item = Item(j, data)
                sum += tmp_item.P_ijk(k, thetas[i]) if delta(X_ij[i][j], k - 1) is True else 0

    return sum
