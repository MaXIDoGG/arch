from itertools import combinations


def comb(n, m):
    x = [i for i in range(n)]
    return list(combinations(x, m))
