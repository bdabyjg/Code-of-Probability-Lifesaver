# Page 101随机抽取葫芦的概率


import random

def full_house_search(num):
    cards = []
    full_house = 0

    for d in range(1, 14):
        for i in range(4):
            cards.append(d)

    for n in range(num):
        hand = sorted(random.sample(cards, 5))
        if hand[0] == hand[1] and hand[3] == hand[4]:
            if hand[2] == hand[1] or hand[2] == hand[3]:
                full_house += 1

    print(f"Percent of time got full house is {100.0 * full_house / num}.")
    print("The prediction were 0.144% and 0.072%.")

# Call the function
full_house_search(10000000)
