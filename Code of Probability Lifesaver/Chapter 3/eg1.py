#======= Page 94的例子=======



import random
import time

def nothin(numdo):
    count = 0
    deck = [i for i in range(1, 14) for _ in range(14)]
    for n in range(numdo):
        card = [0]*14
        hand = random.sample(deck, 5)
        for k in hand:
            card[k] = 1
        if sum(card[1:14]) == 5:
            count += 1
    print("Theory says probability 5 distinct number is ", 2112/41.65, "%.")
    print("Observed probability is ", 100*count/numdo, "%.")

# Start the timer
start_time = time.time()

# Call the function with a specific number
nothin(10000000)

# End the timer and print the elapsed time
end_time = time.time()
print("Elapsed time: ", end_time - start_time, "seconds.")
