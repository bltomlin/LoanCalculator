def differentiated_payment(P, i, n, m):
    d = (P / n) + i * (P - ( (P * (m - 1)) / n))
    return d