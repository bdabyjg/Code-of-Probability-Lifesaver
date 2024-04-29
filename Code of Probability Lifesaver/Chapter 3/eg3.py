#---------------- P120 至少有一个玩家拿到了13张同花色牌

import random
import time

def onesuit(numdo):
    start_time = time.time()
    count = 0
    deck = [i for i in range(1, 53)]
    for n in range(1, numdo+1):
        if n % (numdo // 10) == 0:
            print(f"Have done {100 * n / numdo}%.")
        mix = random.sample(deck, len(deck))
        hands = [mix[i:i + 13] for i in range(0, len(mix), 13)]
        onesuited = 0
        for i in range(4):
            possibleonesuited = 1
            currenthand = hands[i]
            for j in range(1, 13):
                if currenthand[j] // 13 != currenthand[0] // 13:
                    possibleonesuited = 0
            if possibleonesuited > 0:
                onesuited += 1
        if onesuited > 0:
            count += 1
    end_time = time.time()
    print(f"Observed probability is {100 * count / numdo}%.")
    print(f"Execution time: {end_time - start_time} seconds")

# Call the function
onesuit(10000000)
