#============P185  5.3.3错排试验的代码========
import random
import math
import time

def derangement(n, numdo):
    start_time = time.time()  # Record the start time

    count = 0  # Set the counter for success to 0
    # Predict for finite n and n tends to infinity
    theory = sum([(-1)**k/math.factorial(k) for k in range(0, n+1)])
    limit = 1/math.e
    people = [i for i in range(1, n+1)]  # List of people
    # Main loop
    for m in range(1, numdo+1):
        mix = random.sample(people, len(people))  # Randomly mix people
        found = 0  # Set found to 0, if found is 1, then someone's position has not changed
        for i in range(n):
            if mix[i] == people[i]:
                found = 1
                break  # Exit loop
        if found == 1:
            count += 1  # If found equals 1, count plus 1

    end_time = time.time()  # Record the end time
    elapsed_time = end_time - start_time  # Calculate the elapsed time

    print("Theory is ", 100*theory, "%.")
    print("Limit is ", 100*limit, "%.")  # The probability of derangement is equal to 1 - "the probability that someone's position has not changed"
    print("Observe", 100 - 100*count/numdo, "%.")
    print("Elapsed time: ", elapsed_time, "seconds.")  # Print the elapsed time

# Call the function with appropriate parameters
derangement(5, 10000000)
