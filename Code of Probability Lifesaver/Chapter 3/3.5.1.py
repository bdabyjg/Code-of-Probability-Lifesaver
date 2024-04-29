#================ P125将牌的分配===========

import random
from math import comb
from functools import reduce
import time

def fiveohsplit(num):
    start_time = time.time()
    deck = list(range(1, 27))
    count = 0  # 记录得到5-0次数
    for n in range(num):  # 对n循环num次
        handone = sorted(random.sample(deck, 13))
        handtwo = sorted([i for i in deck if i not in handone])
        if sum(handone[:5]) == 15 or sum(handtwo[:5]) == 15:
            count += 1
    print(f"Observed percentage 5-0 is {100 * count / num} %.")
    print(f"Theory from Binomials: {100 * 2 * comb(5, 5) * comb(26 - 5, 13 - 5) / comb(26, 13)} %.")
    print(f"Theory from Cond Prob Prod: {100 * 2 * reduce(lambda x, y: x * y, [(13 - i) / (26 - i) for i in range(5)])} %.")
    print(f"Theory from each card 1/2 chance: {100 * 2 * (1 / 2) ** 5} %.")
    end_time = time.time()
    print(f"Execution time: {end_time - start_time} seconds")

fiveohsplit(1000000)  # Call the function with the desired number of iterations
