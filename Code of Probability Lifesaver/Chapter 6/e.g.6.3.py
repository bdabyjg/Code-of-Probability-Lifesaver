# 划分----P219例子 彩票例子--------
import math

n = 50  # number of items
k = 6   # number of boxes

# Calculate the number of ways using the stars and bars method
ways = math.comb(n + k - 1, k )

print(ways)
# total = 0
# for i1 in range(1, 51):
#     for i2 in range(i1, 51):
#         for i3 in range(i2, 51):
#             for i4 in range(i3, 51):
#                 for i5 in range(i4, 51):
#                     for i6 in range(i5, 51):
#                         total += 1
# print(total)