from fractions import Fraction

# def expected_value(m, n):
#     # 计算每个 E(X_i)
#     term = (Fraction(m - 1, m)) ** n
#     expectation = m * (1 - term)
#     # return expectation
#     return float(expectation)
# # 输入 m 和 n
# m = 6  # 例如 6 个不同颜色的球
# n = 6  # 例如 摸 6 次
#
# # 计算期望值
# E_X = expected_value(m, n)
# # print(f"E(X) = {E_X}")
# print(f"E(X) = {E_X:.3f}")
def expected_value(m, n):
    expectation = 0
    for i in range(1, m + 1):
        # 计算每个 E(I_i)，即第 i 种颜色至少被摸到一次的期望
        prob_not_i = Fraction(m - 1, m) ** n  # 没有摸到第 i 种颜色的概率
        expectation += 1 - prob_not_i  # 加上摸到第 i 种颜色的期望值

    return float(expectation)

# 输入 m 和 n
m = 6  # 例如 6个不同颜色的球
n = 6  # 例如 摸 6 次

# 计算期望值
E_X = expected_value(m, n)
# 输出期望值，保留三位小数
print(f"E(X) = {E_X:.3f}")
